from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome import chrome_options
from time import sleep
persian_digits = "۰۱۲۳۴۵۶۷۸۹"
english_digits = "0123456789"

english_translate = str.maketrans(persian_digits,english_digits)

driver = webdriver.Chrome(options=chrome_options)


columns_3_month = [
    "تاریخ", # 1
    "ساعت", # 2 
    "عنوان اطلاعیه", # 60
    "نماد", # 3 
    "سال مالی", # 4 
    "3 ماهه منتهی به", # 25
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
    "سود(زيان) خالص سه ماهه جاری", # 11
    "سود(زيان) خالص سال گذشته", #  34
    "درصد تغيير", # 12
    "سرمايه‌گذاري‌هاي بلندمدت ", # 35
    "سفارشات و پيش‌پرداخت‌ها ", # 36
    "موجودي مواد و کالا ", # 37
    "موجودي مواد و کالا سال گذشته", #38
    "دريافتني‌هاي تجاري و ساير دريافتني‌ها ", # 39
    "دريافتني‌هاي تجاري و ساير دريافتني‌ها سال گذشته", # 40
    "جمع دارايي‌هاي جاري", # 13 
    "جمع دارايي‌ها", # 14
    "جمع دارايي‌ها سال گذشته" , # 41
    "درصد تغيير", # 42
    "سود(زيان) انباشته", # 43
    "سود(زيان) انباشته سال گذشته", # 44 
    "درصد تغییر" , # 45
    "جمع حقوق مالکانه سه ماهه جاری", # 46 
    "جمع حقوق مالکانه سال گذشته", # 47
    "درصد تغییر", # 48
    "جريان ‌خالص ‌ورود‌ (خروج) ‌نقد حاصل از فعاليت‌هاي ‌عملياتي", # 49
    "جريان ‌خالص ‌ورود‌ (خروج) ‌نقد حاصل از فعاليت‌هاي ‌عملياتي سال گذشته", # 50
    "جريان خالص ورود (خروج) نقد حاصل از فعاليت‌هاي سرمايه‌گذاري ", # 51
    "جريان خالص ورود (خروج) نقد حاصل از فعاليت‌هاي سرمايه‌گذاري سال گذشته", # 52
    "جريان خالص ورود (خروج) نقد حاصل از فعاليت‌هاي تامين مالي ", # 53
    "جريان خالص ورود (خروج) نقد حاصل از فعاليت‌هاي تامين مالي سال گذشته", # 54
    "سود سهام پرداختني ", # 55
    "پيش‌دريافت‌ها", # 56
    "جمع بدهي‌ها", # 57
    "سربارتوليد", # 58
    "هزینه انرژی (آب، برق، گاز و سوخت)", # 59
]

def get_number (x) : 
    return int(str(x).replace(",","").replace(")","").replace("(","").translate(english_translate))


def get_info_3_month (namad,date,url,title) :

    print("start scrapping link 10 code ...")

    new_href = f"{url.split("sheetId")[0]}&sheetId=22"

    driver.get(new_href)
    sleep(.2)

    trs = driver.find_elements(By.XPATH,".//tr")

    hazineh_ha = None

    for tr in trs : 
        tag = driver.execute_script("return arguments[0].innerText",tr)

        if bool ("هزینه" in tag and "انرژ" in tag and "آب" in tag and "گاز" in tag) : 
            tds = tr.find_elements(By.XPATH,".//td")
            hazineh_ha = driver.execute_script("return arguments[0].innerText",tds[1])
            if hazineh_ha : 
                hazineh_ha = str(hazineh_ha).translate(english_translate)

    new_href = f"{url.split("sheetId")[0]}&sheetId=20"

    driver.get(new_href)
    sleep(.2)

    trs = driver.find_elements(By.XPATH,".//tr")

    sarbar_tolid = None

    for tr in trs : 
        tag = driver.execute_script("return arguments[0].innerText",tr)
        
        if bool ("سربار" in tag and "توليد" in tag) :
            tds = tr.find_elements(By.XPATH,".//td")
            sarbar_tolid = driver.execute_script("return arguments[0].innerText",tds[1])
            if sarbar_tolid : 
                sarbar_tolid = str(sarbar_tolid).translate(english_translate)
            break
    

    new_href = f"{url.split("sheetId")[0]}&sheetId=1"

    driver.get(new_href)
    sleep(.2)

    try : 
        div_tags = driver.find_elements(By.CLASS_NAME,"varios")
        sal_mali = driver.execute_script("return arguments[0].innerText",div_tags[5])
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

            if bool("درآمد" in element and "عمليات" in element and "تمام" not in element and "غير" not in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                daramad_amaliati = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                daramad_amaliati_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[3])).translate(english_translate)
                daramad_amaliati_darsad = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)
        

            if bool ("ساير" in element and "درآمدها" in element and "متفرقه" not in element and "غير" not in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                sayer_daramad = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                sayer_daramad_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[3])).translate(english_translate)
                sayer_daramad_darasd = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)
            
            if bool("بهاى" in element and "تمام" in element and "شده" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                bahay_tamam_shodeh = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                bahay_tamam_shodeh_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[3])).translate(english_translate)
                bahay_tamam_shodeh_darsad = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)

            if bool ("ساير" in element and "درآمدها" in element and "هزينه" in element and "غيرعمليات" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                daramd_gher_amaliati = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                daramd_gher_amaliati_sal_ghabl =  str(driver.execute_script("return arguments[0].innerText",tds[3])).translate(english_translate)
                daramd_gher_amaliati_darad = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)

            if bool("سود" in element and "خالص" in element and "عمليات" not in element) and (
                "سهم" not in element and "ناخالص" not in element and "متوقف" not in element
            ) : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_khales = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                sod_khales_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[3])).translate(english_translate)
                sod_khales_darsad = str(driver.execute_script("return arguments[0].innerText",tds[5])).translate(english_translate)

        new_href = f"{url.split("sheetId")[0]}&sheetId=0"

        driver.get(new_href)
        sleep(.2)

        table = driver.find_element(By.CLASS_NAME,"rayanDynamicStatement")
        rows = table.find_elements(By.XPATH,".//tbody/tr")

        sarmaeh_gozari_boland_modat = None
        pish_pardakht_ha = None
        mojodi_mavad = None
        mojodi_mavad_sal_ghabl = None
        daryaft_tegari = None
        daryaft_tegari_sal_ghabl = None

        jam_daraee_jari = None
        jam_daraee = None
        jam_daraee_sal_ghabl = None
        jam_daraee_darsad = None

        sod_anbashteh = None
        sod_anbashteh_sal_ghabl = None
        sod_anbashteh_darsad = None

        hoghogh_malekaneh = None
        hoghogh_malekaneh_sal_ghabl = None
        hoghogh_malekaneh_darsad = None

        sod_saham_pardakhti = None

        pish_daryapht_ha = None
        jam_bedehi_ha = None

        for row in rows :

            element = driver.execute_script("return arguments[0].innerText",row)

            if bool ("جمع" in element and 'بده' in element and "جار" not in element and "حقوق" not in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                jam_bedehi_ha = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)

            # 56 
            if bool ("پيش‌دريافت‌ها" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                pish_daryapht_ha = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)

            # 55 
            if bool ("سود" in element and "سهام" in element and "پرداختن" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_saham_pardakhti = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)

            # 35
            if bool("سرمايه‌گذار" in element and "بلندمدت" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                sarmaeh_gozari_boland_modat = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
            
            # 36 
            if (bool ("سفارشات" in element)) : 
                tds = row.find_elements(By.XPATH,".//td")
                pish_pardakht_ha = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)

            # 37 & 38
            if bool ("موجود" in element and "مواد" in element and "کالا" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                mojodi_mavad = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                mojodi_mavad_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)
            
            # 39 & 40 
            if bool("دريافتن" in element and "تجار" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                daryaft_tegari = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                daryaft_tegari_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)

            if bool("جمع" in element and "دارا" in element and "جار" in element and "غير" not in element) :  
                tds = row.find_elements(By.XPATH,".//td")
                jam_daraee_jari = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
            # 14 , 41 , 42

            if bool ("جمع" in element and "دارا" in element and "جار" not in element ) :
                tds = row.find_elements(By.XPATH,".//td")
                jam_daraee = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                jam_daraee_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)
                jam_daraee_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)
            
            # 43 , 44 , 45
            if bool ("سود" in element and "انباشته" in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_anbashteh = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                sod_anbashteh_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)
                sod_anbashteh_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)
            
            # 46 , 47 , 48 
            if bool ("جمع" in element and "حقوق" in element and "مالکانه" in element and "بده" not in element) : 
                tds = row.find_elements(By.XPATH,".//td")
                hoghogh_malekaneh = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                hoghogh_malekaneh_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(english_translate)
                hoghogh_malekaneh_darsad = str(driver.execute_script("return arguments[0].innerText",tds[4])).translate(english_translate)
            
        if not sarmaeh_gozari_boland_modat : 
            return None
        

        new_href = f"{url.split("sheetId")[0]}&sheetId=9"

        driver.get(new_href)
        sleep(.2)

        table = driver.find_element(By.CLASS_NAME,"rayanDynamicStatement")
        trs = table.find_elements(By.XPATH,".//tr")

        jaryan_amaliaty = None
        jaryan_amaliaty_sal_ghabl = None

        jaryan_sarmayeh = None
        jaryan_sarmayeh_sal_ghabl = None

        jaryan_mali = None
        jaryan_mali_sal_ghabl = None

        for tr in trs : 
            element = driver.execute_script("return arguments[0].innerText",tr)

            # 49 , 50
            if bool ("جريان ‌خالص ‌ورود‌ (خروج) ‌نقد حاصل از فعاليت‌هاي ‌عمليات" in element) : 
                tds = tr.find_elements(By.XPATH,".//td")
                jaryan_amaliaty = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                jaryan_amaliaty_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[3])).translate(english_translate)

            # 51 , 52 
            if bool ("جريان خالص ورود (خروج) نقد حاصل از فعاليت‌ها" in element and "سرمايه‌گذار" in element) : 
                tds = tr.find_elements(By.XPATH,".//td")
                jaryan_sarmayeh = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                jaryan_sarmayeh_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[3])).translate(english_translate)
            
            # 53 , 54 
            if bool ("جريان خالص ورود (خروج) نقد حاصل از فعاليت‌ه" in element and "مال" in element) : 
                tds = tr.find_elements(By.XPATH,".//td")
                jaryan_mali = str(driver.execute_script("return arguments[0].innerText",tds[1])).translate(english_translate)
                jaryan_mali_sal_ghabl = str(driver.execute_script("return arguments[0].innerText",tds[3])).translate(english_translate)

        print("end scraping code 10 .")

        return (
            str(date).translate(english_translate), # 1
            str(time).translate(english_translate), # 2
            title , # 60
            namad, # 3
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
            sod_khales, # 11
            sod_khales_sal_ghabl , # 34
            sod_khales_darsad, # 12
            sarmaeh_gozari_boland_modat, # 35
            pish_pardakht_ha, # 36
            mojodi_mavad, # 37
            mojodi_mavad_sal_ghabl , #38
            daryaft_tegari, # 39
            daryaft_tegari_sal_ghabl, # 40
            jam_daraee_jari, # 13
            jam_daraee, # 14
            jam_daraee_sal_ghabl, # 41
            jam_daraee_darsad, # 42
            sod_anbashteh, # 43
            sod_anbashteh_sal_ghabl, # 44 
            sod_anbashteh_darsad, # 45
            hoghogh_malekaneh, # 46
            hoghogh_malekaneh_sal_ghabl, # 47 
            hoghogh_malekaneh_darsad, # 48
            jaryan_amaliaty, # 49 
            jaryan_amaliaty_sal_ghabl, # 50
            jaryan_sarmayeh, # 51
            jaryan_sarmayeh_sal_ghabl, # 52
            jaryan_mali, # 53
            jaryan_mali_sal_ghabl, # 54
            sod_saham_pardakhti, # 55
            pish_daryapht_ha, # 56
            jam_bedehi_ha, # 57
            sarbar_tolid , # 58
            hazineh_ha, # 59
        )
    except : 
        return None
