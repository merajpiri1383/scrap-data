from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome import chrome_options
persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome(options=chrome_options)


def get_number (x) : 
    return int(str(x).replace(",","").replace(")","").replace("(","").translate(english_translate))


def get_info_3_month (href,date) :

    print("start scrapping link 10 code ...")

    new_href = f"{href.split("sheetId")[0]}&sheetId=1"

    driver.get(new_href)

    try : 
        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = div_tags[5].text if div_tags else None
        saramayed_sabt = div_tags[1].text if div_tags else None
        namad = div_tags[2].text if div_tags else None
        ghozresh_mahianeh = driver.find_element(By.TAG_NAME,"bdo").text
        date,time = date.split(" ")
        return (
            namad,
            str(date).translate(english_translate),
            str(time).translate(english_translate),
            sal_mali,
            saramayed_sabt,
            ghozresh_mahianeh,
        )
    except : 
        return None
    

result = get_info_3_month("https://www.codal.ir/Reports/Decision.aspx?LetterSerial=sCIPpL6UEyoSIZlx3qNy9w%3d%3d&rt=2&let=6&ct=5&ft=7","f f")


print(result)