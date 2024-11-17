from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome import chrome_options
from time import sleep
persian_digits = "۰۱۲۳۴۵۶۷۸۹()"
english_digits = "0123456789  "

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome(options=chrome_options)


columns_3_month = [
    "تاریخ", # 1
    "ساعت", # 2 
    "نماد", # 3 
    "سال مالی", # 4 
    "3 ماهه منتهی به" # 25
    "درآمدهاي عملياتي سه ماهه جاری", # 5
    "درآمدهاي عملياتي سال گذشته", # 26
    "درصد تغيير", # 6 
    "بهاى تمام شده درآمدهاي عملياتي " , # 27
    "بهاى تمام شده درآمدهاي عملياتي سال گذشته" , # 28
    "درصد تغيير", # 29
    "ساير درآمدها سه ماهه جاری" , #30 
    "ساير درآمدها سال گذشته" , # 31 
    "درصد تغيير", # 32
    "ساير درآمدها و هزينه غيرعملياتى سه ماهه جاری", # 9
    "ساير درآمدها و هزينه غيرعملياتى سال گذشته", # 33
    "درصد تغيير", # 10
    # "سود(زيان) ناخالص", # 7 
    # "درصد تغيير", # 8 
    "سود(زيان) خالص سه ماهه جاری", # 11
    "سود(زيان) خالص سال گذشته", #  34
    "درصد تغيير", # 12
    "جمع دارايي‌هاي جاري", # 13 
    "جمع دارايي‌ها", # 14
    "جمع حقوق مالکانه", # 15
    "جمع بدهي‌هاي غيرجاري", # 16 
    "درصد تغيير", # 17 
    "سود سهام پرداختني", # 18
    "جمع بدهي‌هاي جاري", # 19
    "درصد تغيير", # 20 
    "جمع بدهي‌ها", # 21
    "درصد تغيير", # 22
    "جمع حقوق مالکانه و بدهي‌ها", # 23
    "درصد تغيير", # 24
]

def get_number (x) : 
    return int(str(x).replace(",","").replace(")","").replace("(","").translate(english_translate))


def get_info_3_month (namad,date,url) :

    print("start scrapping link 10 code ...")

    new_href = f"{url.split("sheetId")[0]}&sheetId=1"

    driver.get(new_href)
    sleep(.5)

    try : 
        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = div_tags[5].text if div_tags else None
        date,time = date.split(" ")

        semaheh_montahi = driver.execute_script("return arguments[0].innerText",driver.find_element(By.ID,"ctl00_lblPeriodEndToDate"))

        daramad_amaliati = None
        daramad_amaliati_sal_ghabl = None
        daramad_amaliati_darsad = None
        bahay_tamam_shodeh = None
        bahay_tamam_shodeh_sal_ghabl = None
        bahay_tamam_shodeh_darsad = None
        sayer_daramad  = None
        sayer_daramad_sal_ghabl = None
        sayer_daramad_darasd = None
        # sod_na_khales = None
        # sod_na_khales_darsad = None
        daramd_gher_amaliati = None
        daramd_gher_amaliati_sal_ghabl = None
        daramd_gher_amaliati_darad = None
        sod_khales = None
        sod_khales_sal_ghabl = None
        sod_khales_darsad = None

        table = driver.find_element(By.CLASS_NAME,"rayanDynamicStatement")

        rows = table.find_elements(By.XPATH,".//tbody/tr")

        for row in rows : 
            element = driver.execute_script("return arguments[0].innerText",row)

            if bool("عملياتي" in element and "درآمدهاي" in element and "بهاى" not in element) or (
                "عملیاتی" in element and "درآمدهای" in element and "بهاى" not in element
            ) : 
                tds = row.find_elements(By.XPATH,".//td")
                daramad_amaliati = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                daramad_amaliati_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)
                daramad_amaliati_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)

            if bool ("ساير" in element and "درآمدها" in element and "هزينه" not in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                sayer_daramad = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                sayer_daramad_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)
                sayer_daramad_darasd = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)
            
            if bool("بهاى" in element and "تمام" in element and "شده" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                bahay_tamam_shodeh = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                bahay_tamam_shodeh_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)
                bahay_tamam_shodeh_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)

            # if "سود" in element and "ناخالص" in element : 
            #     tds = row.find_elements(By.XPATH,".//td")
            #     sod_na_khales = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
            #     sod_na_khales_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)

            if "غيرعملياتى" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                daramd_gher_amaliati = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                daramd_gher_amaliati_darad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)

            if bool("سود" in element and "خالص" in element and "عمليات" not in element) and (
                "سهم" not in element and "ناخالص" not in element and "متوقف" not in element
            ) : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_khales = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                sod_khales_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)
                sod_khales_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)

        new_href = f"{url.split("sheetId")[0]}&sheetId=0"

        driver.get(new_href)
        sleep(.5)

        table = driver.find_element(By.CLASS_NAME,"rayanDynamicStatement")
        rows = table.find_elements(By.XPATH,".//tbody/tr")

        jam_daraee_jari = None
        jam_daraee = None
        jam_hoghogh_malekaneh = None
        jam_bedehi_ghar_jari = None
        jam_bedehi_ghar_jari_darsad = None
        sod_saham_pardakhtani = None
        jam_bedehi_jari = None
        jam_bedehi_jari_darsad = None
        jam_bedehi = None
        jam_bedehi_darsad = None
        jam_hoghogh_malekaneh_bedehi = None
        jam_hoghogh_malekaneh_bedehi_darsad = None

        for row in rows :

            element = driver.execute_script("return arguments[0].innerText",row)

            if bool("جاری" in element and "دارایی‌های" in element and "جمع" in element and "غیرجاری" not in element) or bool(
                "جاري" in element and "دارايي‌هاي" in element and "جمع" in element and "غیرجاری" not in element
            ) : 
                tds = row.find_elements(By.XPATH,".//td")
                jam_daraee_jari = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)

            if bool("دارايي‌هاي" in element and "جاري" in element and "جمع" in element and "غيرجاري" not in element) or bool(
                "دارایی‌ها" in element and "جاری" not in element and "جمع" in element
            ) :
                tds = row.find_elements(By.XPATH,".//td")
                jam_daraee = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
            
            elif bool("مالکانه" in element and "حقوق" in element and "جمع" in element and "بدهي‌ها" not in element ) : 
                tds = row.find_elements(By.XPATH,".//td")
                jam_hoghogh_malekaneh = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)


            elif bool("غيرجاري" in element and "بدهي‌هاي" in element and "جمع" in element) or bool(
                "غیرجاری" in element and "بدهی‌های" in element and "جمع" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                jam_bedehi_ghar_jari = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                jam_bedehi_ghar_jari_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)
            
            elif bool("سود" in element and "سهام" in element and bool("پرداختنی" in element or "پرداختني" in element)) : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_saham_pardakhtani = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
            
            elif bool("جمع" in element and bool("بدهی‌های" in element or "بدهي‌هاي" in element) and bool("جاري" in element or "جاری" in element)) : 
                tds = row.find_elements(By.XPATH,".//td")
                jam_bedehi_jari = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                jam_bedehi_jari_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)
            
            if bool("جمع" in element and bool("بدهی‌های" in element or "بدهي‌هاي" in element)):  
                tds = row.find_elements(By.XPATH,".//td")
                jam_bedehi = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                jam_bedehi_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)
            
            elif bool("جمع" in element and "حقوق" in element and "مالکانه" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                jam_hoghogh_malekaneh_bedehi = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                jam_hoghogh_malekaneh_bedehi_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)


        print("end scraping code 10 .")
        return (
            namad, # 1
            str(date).translate(english_translate), # 2
            str(time).translate(english_translate), # 3
            sal_mali, # 4
            semaheh_montahi, # 25
            daramad_amaliati, # 5
            daramad_amaliati_sal_ghabl, # 26
            daramad_amaliati_darsad, # 6
            bahay_tamam_shodeh , # 27
            bahay_tamam_shodeh_sal_ghabl, # 28 
            bahay_tamam_shodeh_darsad, # 29
            sayer_daramad, # 30 
            sayer_daramad_sal_ghabl , # 31 ,
            sayer_daramad_darasd , # 32
            daramd_gher_amaliati, # 9
            daramd_gher_amaliati_sal_ghabl, # 33
            daramd_gher_amaliati_darad, # 10 
            # sod_na_khales, # 7 
            # sod_na_khales_darsad, # 8
            sod_khales, # 11
            sod_khales_sal_ghabl , # 34
            sod_khales_darsad, # 12
            jam_daraee_jari, # 13
            jam_daraee, # 14
            jam_hoghogh_malekaneh, # 15
            jam_bedehi_ghar_jari, # 16
            jam_bedehi_ghar_jari_darsad, # 17
            sod_saham_pardakhtani, # 18
            jam_bedehi_jari, # 19
            jam_bedehi_jari_darsad, # 20 
            jam_bedehi, # 21
            jam_bedehi_darsad, # 22 
            jam_hoghogh_malekaneh_bedehi, # 23 
            jam_hoghogh_malekaneh_bedehi_darsad # 24
        )
    except : 
        return None
    

# result = get_info_3_month(
#     url="https://www.codal.ir/Reports/InterimStatement.aspx?LetterSerial=35ZFtuFE9jB6BkUwB1hnTQ%3d%3d",
#     date="۱۴۰۳/۰۸/۲۷ ۱۵:۳۲:۵۱",
#     namad="گنگين"
# )

# print(result)