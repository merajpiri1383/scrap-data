from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from info import get_price


url = "https://codal.ir/ReportList.aspx"

driver = webdriver.Chrome()

driver.get(url)
data = []

table = driver.find_element(By.TAG_NAME,"table")

cols_thead = table.find_elements(By.XPATH,".//thead/tr/th")
rows_tbody = table.find_elements(By.XPATH,".//tbody/tr")


header_row = []
for index,col in enumerate(cols_thead) :    
    if index == 3 : 
        header_row.append("سرمایه ثبت شده")
    if index == 0 or index == 5 :
        header_row.append(col.text) 
data.append(header_row)



for row in rows_tbody : 
    new_row = []
    cols = row.find_elements(By.XPATH,".//td")
    for index,col in enumerate(cols) : 
        if index == 0 : 
            new_row.append(col.text)
        if index == 5 : 
            new_row.append(col.text)
        if index == 3 : 
            tag_a = col.find_element(By.XPATH,".//span/a")
            price = get_price(tag_a.get_property("href"))
            new_row.append(price)
    data.append(new_row)

df = pd.DataFrame(data)

# df.to_csv("export.csv",index=False,header=False)
df.to_excel("export.xlsx",index=False,header=False)

driver.quit()