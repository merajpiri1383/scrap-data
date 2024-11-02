from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome import chrome_options
import asyncio


persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome(options=chrome_options)

async def get_info_30 (href ,date) : 
    driver.get(href)

    print("start link")

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
            yek_mah_montahi = str(tds[16].text.strip()).translate(english_translate)
        except : 
            yek_mah_montahi = 0

        for index,tr in enumerate(trs) : 
            tds = tr.find_elements(By.XPATH,".//td")
            if tds : 
                if "جمع فروش داخلی" in tds[0].text.strip()  : 
                    break
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
            as_ebteday_sal_1 = str(tds[16].text.strip()).translate(english_translate)
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

        try : 
            mablagh_phorosh = str(most_sell["mablagh_phorosh"]).translate(english_translate)
        except : 
            mablagh_phorosh = ""

        try :
            nerkh_phorosh = str(most_sell["nerkh_phorosh"]).translate(english_translate)
        except : 
            nerkh_phorosh = ""

        print("finish")
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
    
urls = [
    {
        "url" : "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=755zzccQOxXFfNj2NERwhQ%3d%3d&rt=0&let=58&ct=0&ft=-1",
        "date" : "d d"
    },
    {
        "url" : "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=lYxN3FLKMiU2SnhkukA5xQ%3d%3d&rt=0&let=58&ct=0&ft=-1",
        "date" : "r r"
    },
    {
        "url" : "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=kiytceRd9SMRJVq3tzlpZA%3d%3d&rt=0&let=58&ct=0&ft=-1",
        "date" : "r e"
    },
    {
        "url" : "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=wCi2y5150WzxDmS9NL0W0g%3d%3d&rt=5&let=58&ct=0&ft=-1",
        "date" : "e w"
    },
    {
        "url" : "https://www.codal.ir/Reports/Decision.aspx?LetterSerial=feJHgCHe6UJPYVN97DBgJw%3d%3d&rt=0&let=58&ct=0&ft=-1",
        "date" : "w e"
    }
]



# def main () : 

#     loop = asyncio.new_event_loop()
#     tasks = []

#     for item in urls : 
#         new_task = loop.create_task(get_info_30(item["url"],item["date"]))
#         tasks.append(new_task)

#     results = asyncio.gather(*tasks)
#     loop.run_until_complete(results)

#     for item in results.result() :
#         print(item)


# main()
