from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome import chrome_options

persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome(options=chrome_options)

def get_info_30 (href ,date) : 
    driver.get(href)

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
        tds = last_tr.find_elements(By.TAG_NAME,"td")
        jam_phorosh_dahkeli = 0

        for index,tr in enumerate(trs) : 
            tds = tr.find_elements(By.XPATH,".//td")
            if tds : 
                if "جمع فروش داخلی" in tds[0].text.strip()  : 
                    break
                elif index < 3 :
                    continue
                else : 
                    try : 
                        result = int(str(tds[16].text.strip().replace(",","")).translate(english_translate))
                        if most_sell["product"] < result : 
                            most_sell = {
                                "product" : result,
                                "name" : tds[0].text.strip()
                            }
                            try :
                                most_sell["nerkh_phorosh"] = driver.execute_script("return arguments[0].innerText",tds[23])
                            except : 
                                pass 

                            try : 
                                most_sell["mablagh_phorosh"] = driver.execute_script("return arguments[0].innerText",tds[24])
                            except : 
                                pass
                    except : 
                        pass

        try : 
            for index,tr in enumerate(trs) : 
                if "جمع فروش داخلی" in tr.text : 
                    jam_phorosh_dahkeli = tr.find_elements(By.XPATH,"./td")[16].text.strip()
        except : 
            jam_phorosh_dahkeli = 0



        try : 
            yek_mah_montahi = tds[12].text.strip() 
        except : 
            yek_mah_montahi = 0
        
        try : 
            as_ebteday_sal_1 = tds[16].text.strip()
        except : 
            as_ebteday_sal_1 = 0

        try : 
            as_ebteday_sal_2 = driver.execute_script("return arguments[0].innerText",tds[-2])
        except : 
            as_ebteday_sal_2 = 0

        date,time = date.split(" ")


        return (
            namad,
            str(date).translate(english_translate),
            str(time).translate(english_translate),
            sal_mali,
            saramayed_sabt,
            ghozresh_mahianeh,
            yek_mah_montahi.translate(english_translate),
            as_ebteday_sal_1.translate(english_translate),
            str(as_ebteday_sal_2).translate(english_translate),
            str(jam_phorosh_dahkeli).translate(english_translate),
            most_sell["name"],
            str(most_sell["mablagh_phorosh"]).translate(english_translate),
            str(most_sell["nerkh_phorosh"]).translate(english_translate),
        )
    except : 
        return None