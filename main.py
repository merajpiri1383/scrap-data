import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from page import get_list_of_sams


url = "https://codal.ir/ReportList.aspx"

driver = webdriver.Chrome()

data = []



data.append(
    ("نماد","سال مالی","سرمایه ثبت شده","گزارش فعالیت ماهیانه منتهی","دوره یک ماه منتهی","از ابتدای سال مالی")
)

page = 1
while page < 100 : 
    url = f"https://codal.ir/ReportList.aspx?PageNumber={page}"
    data = data + get_list_of_sams(url)
    page = page + 1




df = pd.DataFrame(data)

# df.to_csv("export.csv",index=False,header=False)
df.to_excel("export.xlsx",index=False,header=False)

driver.quit()