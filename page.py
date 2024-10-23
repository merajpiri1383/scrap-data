from selenium import webdriver
from selenium.webdriver.common.by import By
from info import get_info


driver = webdriver.Chrome()


data = []

def get_list_of_sams (href) :

    driver.get(href)
    table = driver.find_element(By.TAG_NAME,"table")
    rows_tbody = table.find_elements(By.XPATH,".//tbody/tr")

    for row in rows_tbody : 
        cols = row.find_elements(By.XPATH,".//td")
        for index,col in enumerate(cols) : 
            if index == 3 : 
                tag_a = col.find_element(By.XPATH,".//span/a")
                if "گزارش" in tag_a.text : 
                    result = get_info(tag_a.get_property("href"))
                    if result : 
                        data.append(result)
    return data