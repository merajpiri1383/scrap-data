from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def get_price (href ) : 


    driver.get(href)

    div_tags = driver.find_elements(By.CLASS_NAME,"varios")
    if div_tags : 
        return div_tags[1].text