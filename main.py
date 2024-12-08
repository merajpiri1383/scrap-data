import pandas as pd
from selenium import webdriver
from jdatetime import datetime
from page import get_list_of_sams
from chrome import chrome_options
from info_12_month import columns_12_month
from info_3_month import columns_3_month
from info_code_30 import columns_30
from info_code_31 import columns_31


file_name = f"Data {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.xlsx"


url = "https://codal.ir/ReportList.aspx"

driver = webdriver.Chrome(options=chrome_options)



data_month = []
data_3_month = []
data_year = []
data_month_31 = []


def get_by_date (from_date,to_date,codes=[]) :

    print("start ...")

    f = str(from_date).replace("/","%2F")
    t = str(to_date).replace("/","%2F")
    page = 1

    while page < 10 : 
        page = page + 1
        url = f"https://codal.ir/ReportList.aspx?search&LetterType=-1&FromDate={f}&ToDate={t}&PageNumber={page}"
        print("start scraping page ", page)
        month,data_31,three_month,year = get_list_of_sams(url,codes=codes)

        for item in data_31 : 
            data_month.append(item)
        
        for item in month : 
            data_month.append(item)

        for item in three_month : 
            data_3_month.append(item)
        
        for item in year : 
            data_year.append(item)
    
    data_1 = pd.DataFrame(data=list(set(data_month)),columns=columns_30)
    data_2 = pd.DataFrame(data=list(set(data_month_31)),columns=columns_31)
    data_3 = pd.DataFrame(data=list(set(data_year)),columns=columns_12_month)
    data_4 = pd.DataFrame(data=list(set(data_3_month)),columns=columns_3_month)

    data_1.to_excel(file_name,engine="openpyxl",index=False,sheet_name="گزارش ماهانه ن-۳۰")

    with pd.ExcelWriter(file_name,engine="openpyxl",mode="a") as writer : 
        data_2.to_excel(writer,sheet_name="گزارش ماهانه ن-۳۱",index=False)
        data_3.to_excel(writer,sheet_name="گزارش سالیانه",index=False)
        data_4.to_excel(writer,sheet_name="سه ماهه",index=False)