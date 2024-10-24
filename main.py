import pandas as pd
from selenium import webdriver
from datetime import datetime
from page import get_list_of_sams

file_name = f"Data {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.xlsx"


url = "https://codal.ir/ReportList.aspx"

driver = webdriver.Chrome()

columns = ["نماد","زمان","سال مالی","سرمایه ثبت شده","گزارش فعالیت ماهیانه منتهی","دوره یک ماه منتهی","از ابتدای سال مالی"]

data_month = []
data_6_month = []
data_year = []


page = 1
while page < 301 : 
    url = f"https://codal.ir/ReportList.aspx?PageNumber={page}"
    month,six_month,year = get_list_of_sams(url)
    data_month = list(set( data_month + month))
    data_6_month = list(set(data_6_month + six_month))
    data_year = list(set(data_year + year))
    page = page + 1


data_1 = pd.DataFrame(data=data_month,columns=columns)
data_2 = pd.DataFrame(data=data_6_month,columns=columns)
data_3 = pd.DataFrame(data=data_year,columns=columns)

data_1.to_excel(file_name,engine="openpyxl",index=False,sheet_name="گزارش ماهانه")

with pd.ExcelWriter(file_name,engine="openpyxl",mode="a") as writer : 
    data_2.to_excel(writer,sheet_name="گزارش ۶ ماه",index=False)
    data_3.to_excel(writer,sheet_name="گزارش سالانه",index=False)

driver.quit()