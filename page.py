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
code_month_2 = "ن-۳۱"


def get_row (code,rows_tbody) : 
    for row in rows_tbody :
        if code in row.text : 
            cols = row.find_elements(By.XPATH,".//td")
            tag_a = None
            date = None
            for index,col in enumerate(cols) : 
                if index == 6 : 
                    date = col.text
                if index == 3 : 
                    tag_a = col.find_element(By.XPATH,".//span/a")
            if tag_a : 
                if code == code_month_2 : 
                    result = get_info(tag_a.get_property("href"),date,True)
                else : 
                    result = get_info(tag_a.get_property("href"),date)
                try : 
                    if result[0] : 
                        if code == code_month_2 : 
                            data_month.append(result)
                        if code == code_month : 
                            data_month.append(result)
                        elif code == code_6_month : 
                            data_6_month.append(result)
                        elif code == code_year : 
                            data_year.append(result)
                except : 
                    pass 

def get_list_of_sams (href) :

    driver.get(href)
    table = driver.find_element(By.TAG_NAME,"table") 
    rows_tbody = table.find_elements(By.XPATH,".//tbody/tr")

    get_row(code_month,rows_tbody)
    get_row(code_month_2,rows_tbody)
    get_row(code_6_month,rows_tbody)
    get_row(code_year,rows_tbody)

    return (
        data_month,
        data_6_month,
        data_year
    )


# result = get_list_of_sams("https://codal.ir/ReportList.aspx")

# print(result)