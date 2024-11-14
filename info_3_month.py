from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome import chrome_options
persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome(options=chrome_options)


columns_3_month = [
    "تاریخ",
    "ساعت",
    "نماد",
    "سال مالی",
    "درآمدهاي عملياتي",
    "درصد تغيير",
    "سود(زيان) ناخالص",
    "درصد تغيير",
    "ساير درآمدها و هزينه غيرعملياتى",
    "درصد تغيير",
    "سود(زيان) خالص",
    "درصد تغيير",
    "جمع دارايي‌هاي جاري",
    "جمع دارايي‌ها",
    "جمع حقوق مالکانه",
    "جمع بدهي‌هاي غيرجاري",
    "درصد تغيير",
    "سود سهام پرداختني",
    "جمع بدهي‌هاي جاري",
    "درصد تغيير",
    "جمع بدهي‌ها",
    "درصد تغيير",
    "جمع حقوق مالکانه و بدهي‌ها",
    "درصد تغيير",
]

def get_number (x) : 
    return int(str(x).replace(",","").replace(")","").replace("(","").translate(english_translate))


def get_info_3_month (namad,date,url) :

    print("start scrapping link 10 code ...")

    new_href = f"{url.split("sheetId")[0]}&sheetId=1"

    driver.get(new_href)

    try : 
        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = div_tags[5].text if div_tags else None
        date,time = date.split(" ")

        daramad_amaliati = None
        daramad_amaliati_darsad = None
        sod_na_khales = None
        sod_na_khales_darsad = None
        daramd_gher_amaliati = None
        daramd_gher_amaliati_darad = None
        sod_khales = None
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
                daramad_amaliati_darsad = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)

            if "سود" in element and "ناخالص" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_na_khales = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                sod_na_khales_darsad = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)

            if "غيرعملياتى" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                daramd_gher_amaliati = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                daramd_gher_amaliati_darad = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)

            if bool("سود" in element and "خالص" in element and "عمليات" not in element) and (
                "سهم" not in element and "ناخالص" not in element and "متوقف" not in element
            ) : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_khales = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                sod_khales_darsad = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)
        
        new_href = f"{url.split("sheetId")[0]}&sheetId=0"

        driver.get(new_href)

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
            namad,
            str(date).translate(english_translate),
            str(time).translate(english_translate),
            sal_mali,
            daramad_amaliati,
            daramad_amaliati_darsad,
            sod_na_khales,
            sod_na_khales_darsad,
            daramd_gher_amaliati,
            daramd_gher_amaliati_darad,
            sod_khales,
            sod_khales_darsad,
            jam_daraee_jari,
            jam_daraee,
            jam_hoghogh_malekaneh,
            jam_bedehi_ghar_jari,
            jam_bedehi_ghar_jari_darsad,
            sod_saham_pardakhtani,
            jam_bedehi_jari,
            jam_bedehi_jari_darsad,
            jam_bedehi,
            jam_bedehi_darsad,
            jam_hoghogh_malekaneh_bedehi,
            jam_hoghogh_malekaneh_bedehi_darsad
        )
    except : 
        return None,