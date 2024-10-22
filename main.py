from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time



url = "https://codal.ir/Reports/Decision.aspx?LetterSerial=QQQaQQQeGQQQaQQQ6LTaipNhvmAbeVtyCQ%3d%3d&rt=0&let=58&ct=0&ft=-1"

driver = webdriver.Chrome()

driver.get(url)
time.sleep(5)

soup = BeautifulSoup(driver.page_source,"html.parser")

table = soup.find("table")

rows = table.find_all("tr")

table_data = []

for row in rows : 
    cols = row.find_all(["td","th"])
    cols = [col.text.strip() for col in cols]
    table_data.append(cols)

df = pd.DataFrame(table_data)

df.to_excel("export.xlsx",index=False,header=False)

driver.quit()