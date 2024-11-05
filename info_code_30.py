from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome import chrome_options
import asyncio


persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome(options=chrome_options)

def get_info_30 (href ,date,data=[]) : 
    driver.get(href)

    print("start scrapping link 30 code ...")

    most_sell = {
        "product" : 0,
        "name" : None
    }
    
    try : 

        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = div_tags[5].text.strip() if div_tags else None
        saramayed_sabt = div_tags[1].text.strip() if div_tags else 0
        namad = div_tags[2].text.strip() if div_tags else None
        ghozresh_mahianeh = driver.find_element(By.TAG_NAME,"bdo").text.strip()
        table = driver.find_elements(By.TAG_NAME,"table")[0]
        trs = table.find_elements(By.TAG_NAME,"tr")
        last_tr = trs[-1]
        tds = last_tr.find_elements(By.XPATH,".//td")
        jam_phorosh_dahkeli = 0

        try : 
            yek_mah_montahi = str(driver.execute_script("return arguments[0].innerText",tds[16])).translate(english_translate)
        except : 
            yek_mah_montahi = 0

        for index,tr in enumerate(trs) : 
            tds = tr.find_elements(By.XPATH,".//td")

            if tds : 
                if "جمع" in tds[0].text.strip()  : 
                    continue
                elif index < 3 :
                    continue
                else : 
                    try : 

                        result = int(str(driver.execute_script("return arguments[0].innerText",tds[16]).replace(",","")).translate(english_translate))
                        if most_sell["product"] < result : 
                            most_sell = {
                                "product" : result,
                                "name" : tds[0].text.strip()
                            }
                            try :
                                most_sell["nerkh_phorosh"] = driver.execute_script("return arguments[0].innerText",tds[15])
                            except : 
                                pass 

                            try : 
                                most_sell["mablagh_phorosh"] = driver.execute_script("return arguments[0].innerText",tds[16])
                            except : 
                                pass
                    except : 
                        pass

        try : 
            for index,tr in enumerate(trs) : 
                if "جمع فروش داخلی" in tr.text : 
                    jam_phorosh_dahkeli = driver.execute_script("return arguments[0].innerText",tr.find_elements(By.XPATH,"./td")[16])
        except : 
            jam_phorosh_dahkeli = 0
    
        try : 
            as_ebteday_sal_1 = str(driver.execute_script("return arguments[0].innerText",tds[12])).translate(english_translate)
        except : 
            as_ebteday_sal_1 = 0

        try : 
            as_ebteday_sal_2 = str(driver.execute_script("return arguments[0].innerText",tds[-2])).translate(english_translate)
        except : 
            as_ebteday_sal_2 = 0

        date,time = date.split(" ")

        try : 
            most_sell_name = most_sell["name"]
        except : 
            most_sell_name = ""

        mablagh_phorosh = str(most_sell["mablagh_phorosh"]).translate(english_translate)
        nerkh_phorosh = str(most_sell["nerkh_phorosh"]).translate(english_translate)
        
        print("end scrapping link 30 code ")

        return (
            namad,
            str(date).translate(english_translate),
            str(time).translate(english_translate),
            sal_mali,
            saramayed_sabt,
            ghozresh_mahianeh,
            yek_mah_montahi,
            as_ebteday_sal_1,
            as_ebteday_sal_2,
            str(jam_phorosh_dahkeli).translate(english_translate),
            most_sell_name,
            mablagh_phorosh,
            nerkh_phorosh
        )
    except : 
        return None
    

result = get_info_30("https://www.codal.ir/Reports/Decision.aspx?LetterSerial=QtnlOMOOObOOO2SQvHMBbgzURykA%3d%3d&rt=0&let=58&ct=0&ft=-1","f f")


print(result)