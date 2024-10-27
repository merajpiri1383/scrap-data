from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome()


def get_number (x) : 
    return int(str(x).replace(",","").replace(")","").replace("(","").translate(english_translate))

def get_most_price_company (table,table_2) : 
    
    most = {
        "name" : None,
        "price" : 0
    }

    trs_table_2 = table_2.find_elements(By.XPATH,"./tbody/tr")
    
    trs = table.find_elements(By.XPATH,"./tbody/tr")

    for index,tr in enumerate(trs) : 
        tds = tr.find_elements(By.XPATH,"./td")
        if tds : 
            result = get_number(tds[7].text.strip())
            if result > most["price"] : 
                most = {
                    "price" : result,
                    "name" : trs_table_2[index].text.strip() if trs_table_2 else None
                }
    return most["name"]


def get_info_code_31 (href,date) : 

    new_href = f"{href.split("sheetId")[0]}&sheetId=4"


    driver.get(new_href)

    try : 
        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = div_tags[5].text if div_tags else None
        saramayed_sabt = div_tags[1].text if div_tags else None
        namad = div_tags[2].text if div_tags else None
        ghozresh_mahianeh = driver.find_element(By.TAG_NAME,"bdo").text
        date,time = date.split(" ")
        try :
            table = driver.find_elements(By.XPATH,".//table")
            if table : 
                table_2 = table[3]
                table = table[4]
            
            try :
                most_price_company = get_most_price_company(table,table_2)
            except : 
                most_price_company = ""
            if table : 
                last_row = table.find_element(By.XPATH,"./tfoot/tr")
            if last_row : 
                tds = last_row.find_elements(By.XPATH,"./td")
            try : 
                bahayeh_tamam_shodeh = tds[6].text.strip()
            except : 
                bahayeh_tamam_shodeh = 0
            
            try : 
                arzesh_bazar = tds[7].text.strip()
            except : 
                arzesh_bazar = 0
        except : 
            table = driver.find_elements(By.XPATH,".//table")[0]
            trs = table.find_elements(By.XPATH,".//tr")
            most = 0

            last_row = trs[-1]
            tds = last_row.find_elements(By.XPATH,".//td")
            bahayeh_tamam_shodeh = tds[10].text.strip()
            arzesh_bazar = tds[11].text.strip()


            for num,tr in enumerate(trs) : 
                tds = tr.find_elements(By.XPATH,".//td")
                if len(tds) > 3 : 
                    if tr != trs[0] and tr != trs[-1] and "سهام" not in tr.text : 
                        try :
                            price = get_number(tds[11].text.strip())
                            if price > most : 
                                most = tds[0].text.strip()
                        except  :
                            pass 
                most_price_company = most
                    

    
        return (
            namad,
            str(date).translate(english_translate),
            str(time).translate(english_translate),
            sal_mali,
            saramayed_sabt,
            ghozresh_mahianeh,
            str(bahayeh_tamam_shodeh).translate(english_translate),
            str(arzesh_bazar).translate(english_translate),
            most_price_company
        )
    except :
        return None