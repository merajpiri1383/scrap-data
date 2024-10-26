from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome()

def get_info_30 (href ,date) : 
    driver.get(href)

    
    
    # try : 
        
    #     div_tags = driver.find_elements(By.CLASS_NAME,"varios")
    #     sal_mali = div_tags[5].text.strip() if div_tags else None
    #     saramayed_sabt = div_tags[1].text.strip() if div_tags else 0
    #     namad = div_tags[2].text.strip() if div_tags else None
    #     ghozresh_mahianeh = driver.find_element(By.TAG_NAME,"bdo").text.strip()
    #     table = driver.find_elements(By.TAG_NAME,"table")[0]
    #     trs = table.find_elements(By.TAG_NAME,"tr")
    #     last_tr = trs[-1]
    #     tds = last_tr.find_elements(By.TAG_NAME,"td")
    #     jam_phorosh_dahkeli = 0
    #     product_row = 0

    #     try : 
    #         for index,tr in enumerate(trs) : 
    #             if "جمع فروش داخلی" in tr.text : 
    #                 product_row = trs[index - 2]
    #                 jam_phorosh_dahkeli = tr.find_elements(By.XPATH,"./td")[16].text.strip()
    #     except : 
    #         jam_phorosh_dahkeli = 0


    #     mahsol = str(product_row.find_elements(By.XPATH,"./td")[16].text.strip()).translate(english_translate)
        


    #     try : 
    #         yek_mah_montahi = tds[12].text.strip() 
    #     except : 
    #         yek_mah_montahi = 0
        
    #     try : 
    #         as_ebteday_sal_1 = tds[16].text.strip()
    #     except : 
    #         as_ebteday_sal_1 = 0

    #     try : 
    #         as_ebteday_sal_2 = driver.execute_script("return arguments[0].innerText",tds[-2])
    #     except : 
    #         as_ebteday_sal_2 = 0

    #     date,time = date.split(" ")


    #     return (
    #         namad,
    #         str(date).translate(english_translate),
    #         str(time).translate(english_translate),
    #         sal_mali,
    #         saramayed_sabt,
    #         ghozresh_mahianeh,
    #         yek_mah_montahi.translate(english_translate),
    #         as_ebteday_sal_1.translate(english_translate),
    #         str(as_ebteday_sal_2).translate(english_translate),
    #         str(jam_phorosh_dahkeli).translate(english_translate),
    #         mahsol,
    #     )
    # except : 
    #     return None



result = get_info_30("https://www.codal.ir/Reports/Decision.aspx?LetterSerial=QKQQiUMIOOOObOOOl5boEhnOQQQaQQQcNA%3d%3d&rt=0&let=58&ct=0&ft=-1","f f")


def get_info_code_31 (href,date) : 

    new_href = f"{href.split("sheetId")[0]}&sheetId=3"

    driver.get(new_href)

    try : 
        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = div_tags[5].text if div_tags else None
        saramayed_sabt = div_tags[1].text if div_tags else None
        namad = div_tags[2].text if div_tags else None
        ghozresh_mahianeh = driver.find_element(By.TAG_NAME,"bdo").text

        table = driver.find_elements(By.TAG_NAME,"table")[0]
        last_tr = table.find_elements(By.TAG_NAME,"tr")[-1]
        tds = last_tr.find_elements(By.TAG_NAME,"td")
        yek_mah_montahi = tds[7].text
        bazar_arzesh = tds[8].text
        date,time = date.split(" ")

    
        return (
            namad,
            str(date).translate(english_translate),
            str(time).translate(english_translate),
            sal_mali,
            saramayed_sabt,
            ghozresh_mahianeh,
            str(yek_mah_montahi).translate(english_translate),
            str(bazar_arzesh).translate(english_translate)
        )
    except : 
        return None