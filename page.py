from selenium import webdriver
from selenium.webdriver.common.by import By
from info import get_info


driver = webdriver.Chrome()


data_month = []
data_6_month = []
data_year = []

code_month = "ن-۳۰"
code_6_month = "ن-۱۰"
code_year = "ن-۵۲"


def get_row (code,rows_tbody) : 
    for row in rows_tbody :
        if code in code in row.text : 
            cols = row.find_elements(By.XPATH,".//td")
            for index,col in enumerate(cols) : 
                if index == 3 : 
                    tag_a = col.find_element(By.XPATH,".//span/a")
                    result = get_info(tag_a.get_property("href"))
                    if result : 
                        if code == code_month : 
                            data_month.append(result)
                        elif code == code_6_month : 
                            data_6_month.append(result)
                        elif code == code_year : 
                            data_year.append(result)

def get_list_of_sams (href) :

    driver.get(href)
    table = driver.find_element(By.TAG_NAME,"table") 
    rows_tbody = table.find_elements(By.XPATH,".//tbody/tr")

    get_row(code_month,rows_tbody)
    get_row(code_6_month,rows_tbody)
    get_row(code_year,rows_tbody)

    return (
        data_month,
        data_6_month,
        data_year
    )
    


# result = get_list_of_sams("https://codal.ir/ReportList.aspx?PageNumber=4")

# for item in result : 
#     print(item)