from selenium import webdriver
from selenium.webdriver.common.by import By
from info_code_30 import get_info_30
from info_code_31 import get_info_code_31
from time import sleep
from chrome import chrome_options



driver = webdriver.Chrome(options=chrome_options)

data_month = []
data_6_month = []
data_year = []
data_month_31 = []

code_month = "ن-۳۰"
code_6_month = "ن-۱۰"
code_year = "ن-۵۲"
code_month_31 = "ن-۳۱"

list_href_31 = [
]


def get_links (code,rows_tbody) : 
    links = []
    try :
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
                    links.append(
                            {
                                "url" : tag_a.get_property("href"),
                                "date" : date
                            }
                        )
    except : 
        pass
    return links    


def get_list_of_sams (href) :


    driver.get(href)
    sleep(1)
    table = driver.find_element(By.TAG_NAME,"table") 
    rows_tbody = table.find_elements(By.XPATH,".//tbody/tr")

    links_30 =  get_links(code_month,rows_tbody)
    links_31 = get_links(code_month_31,rows_tbody)

    for link in links_30 : 
        result = get_info_30(link["url"],link["date"])
        if result and len(result) == 13 : 
            print(result)
            data_month.append(result)
    
    for link in links_31 : 
        result = get_info_code_31(link["url"],link["date"])
        if result and len(result) == 10 : 
            print(result)
            data_month_31.append(result)
        

    return (
        data_month,
        data_month_31,
        data_6_month,
        data_year
    )


# result = get_list_of_sams("https://codal.ir/ReportList.aspx?PageNumber=49")