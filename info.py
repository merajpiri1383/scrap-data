from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# href= "https://codal.ir/Reports/MonthlyActivity.aspx?LetterSerial=CZO9Csi5eBTXRBD3NtAw7w%3d%3d"
href= "https://codal.ir/Reports/MonthlyActivity.aspx?LetterSerial=QiyUT19VORd7YxMfnfbLsA%3d%3d"

def get_info (href ) : 


    driver.get(href)

    try : 
        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = div_tags[5].text if div_tags else None
        saramayed_sabt = div_tags[1].text if div_tags else None
        namad = div_tags[2].text if div_tags else None
        ghozresh_mahianeh = driver.find_element(By.TAG_NAME,"bdo").text
        spans = driver.find_elements(By.CLASS_NAME,"dynamic_comp")
        try : 
            yek_mah_montahi = spans[120].text
            as_ebteday_sal = spans[116].text 
        except : 
            as_ebteday_sal = ""
            yek_mah_montahi = ""
        return (
            namad,
            sal_mali,
            saramayed_sabt,
            ghozresh_mahianeh,
            yek_mah_montahi,
            as_ebteday_sal,
        )
    except : 
        return None
    

# result = get_info(href=href)

# print(result)