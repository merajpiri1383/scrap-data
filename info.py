from selenium import webdriver
from selenium.webdriver.common.by import By

persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome()

href= "https://codal.ir/Reports/MonthlyActivity.aspx?LetterSerial=QiyUT19VORd7YxMfnfbLsA%3d%3d"

def get_info (href ,date,is_code_31=False) : 


    driver.get(href)

    try : 
        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = div_tags[5].text if div_tags else None
        saramayed_sabt = div_tags[1].text if div_tags else None
        namad = div_tags[2].text if div_tags else None
        ghozresh_mahianeh = driver.find_element(By.TAG_NAME,"bdo").text
        spans = driver.find_elements(By.CLASS_NAME,"dynamic_comp")

        if is_code_31 : 
            try : 
                yek_mah_montahi = spans[14].text
                as_ebteday_sal = spans[15].text 
            except : 
                as_ebteday_sal = ""
                yek_mah_montahi = ""
        else : 
            try : 
                yek_mah_montahi = spans[120].text
                as_ebteday_sal = spans[116].text 
            except : 
                as_ebteday_sal = ""
                yek_mah_montahi = ""
        return (
            namad,
            str(date).translate(english_translate),
            sal_mali,
            saramayed_sabt,
            ghozresh_mahianeh,
            yek_mah_montahi.translate(english_translate),
            as_ebteday_sal.translate(english_translate),
        )
    except : 
        return None