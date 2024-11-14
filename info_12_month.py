from selenium.webdriver import Chrome
from chrome import chrome_options
from selenium.webdriver.common.by import By

persion_numbers = "۰۱۲۳۴۵۶۷۸۹"
english_numbers = "0123456789"

translate_text = str.maketrans(persion_numbers,english_numbers)


driver = Chrome(options=chrome_options)


columns_12_month = [
    "تاریخ",
    "ساعت",
    "نماد",
    "سود (زیان) انباشته شده پایان دوره",
    "سود سهام مصوب (مجمع سال جاری)",
    "سود (زیان) انباشته پايان دوره",
    "سود (زیان) خالص هر سهم- ریال",
    "سود نقدی هر سهم (ریال)",
    "سود (زیان) انباشته ابتدای دوره تعدیل‌شده",
    "سود سهام مصوب (مجمع سال قبل)",
    "سهامدار ۱",
    "درصد مالکیت",
    "مبلغ",
    "سهامدار ۲",
    "درصد مالکیت",
    "مبلغ",
    "سهامدار ۳",
    "درصد مالکیت",
    "مبلغ",
    "سهامدار ۴",
    "درصد مالکیت",
    "مبلغ",
    "سهامدار ۵",
    "درصد مالکیت",
    "مبلغ",
]




def get_info_12_month (url,date,namad) : 

    driver.get(url)

    saham_daran_table = driver.find_element(By.ID,"ucAssemblyShareHolder1_gvAssemblyShareHolder")

    date ,time = date.split(" ")

    saham_daran_list = []

    print("start scraping 12 month code ...")

    rows = saham_daran_table.find_elements(By.XPATH,".//tr")

    tds = rows[3].find_elements(By.XPATH,".//td")


    for row in rows : 
        element = driver.execute_script("return arguments[0].innerText",row)
        if "جمع" not in element : 
            tds = row.find_elements(By.XPATH,".//td")
            if len(tds) > 2 : 
                data = {
                    "name" : tds[0].text.strip(),
                    "sahm" : tds[1].text.strip(),
                    "percent" : int(float(tds[2].text.strip().split(" ")[0])),
                }
                saham_daran_list.append(data)
    
    saham_daran_list.sort(key=lambda x : x["percent"],reverse=True)
    saham_daran_list = saham_daran_list[0:5]

    try : 
        sahm_1 = saham_daran_list[0]
    except : 
        sahm_1 = {"name": None,"sahm" : 0,"percent" : None}
    
    try : 
        sahm_2 = saham_daran_list[1]
    except : 
        sahm_2 = {"name": None,"sahm" : 0,"percent" : None}
    
    try : 
        sahm_3 = saham_daran_list[2]
    except : 
        sahm_3 = {"name": None,"sahm" : 0,"percent" : None}

    try : 
        sahm_4 = saham_daran_list[3]
    except : 
        sahm_4 = {"name": None,"sahm" : 0,"percent" : None}
    
    try :
        sahm_5 = saham_daran_list[4]
    except : 
        sahm_5 = {"name": None,"sahm" : 0,"percent" : None}

    sod_table = driver.find_element(By.ID,"ucAssemblyPRetainedEarning_grdAssemblyProportionedRetainedEarning")

    rows_sod_table = sod_table.find_elements(By.XPATH,".//tr")

    sod_naghdi_har_sahm = None
    sod_khales_har_sahm = None
    sod_anbashteh_payan_doreh = None
    sod_saham_mosavab_jari = None
    sod_anbashteh_payan_doreh_mosavabat = None
    sod_anbashted_ebreday_doreh = None
    sod_sal_ghabl = None

    if len (rows_sod_table) > 3 : 
        for index,row in enumerate(rows_sod_table) : 
            element = driver.execute_script("return arguments[0].innerText",row)
            if "انباشته پايان دوره" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_anbashteh_payan_doreh = str(driver.execute_script(
                    "return arguments[0].innerText",tds[2])
                ).translate(translate_text)
            if "سود نقدی هر سهم" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_naghdi_has_sahm = str(driver.execute_script(
                    "return arguments[0].innerText",tds[2])
                ).translate(translate_text)
            
            if "سهام مصوب" in element and "جاری" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_saham_mosavab_jari = str(driver.execute_script(
                    "return arguments[0].innerText",tds[2])
                ).translate(translate_text)
            
            if "لحاظ نمودن مصوبات مجمع" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_anbashteh_payan_doreh_mosavabat = str(driver.execute_script(
                    "return arguments[0].innerText",tds[2])
                ).translate(translate_text)

            if "خالص هر سهم" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_khales_har_sahm = str(driver.execute_script(
                    "return arguments[0].innerText",tds[2])
                ).translate(translate_text)
            
            if "نقدی هر سهم" in element : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_naghdi_har_sahm = str(driver.execute_script(
                    "return arguments[0].innerText",tds[2])
                ).translate(translate_text)
            
            if "انباشته ابتدای دوره تعدیل‌شده" in element : 
                sod_anbashted_ebreday_doreh = str(driver.execute_script(
                    "return arguments[0].innerText",tds[2])
                ).translate(translate_text)

            if "سود سهام مصوب (مجمع سال قبل)" in element : 
                sod_sal_ghabl = str(driver.execute_script(
                    "return arguments[0].innerText",tds[2])
                ).translate(translate_text)

    print("end scraping 12 month code .")
    return (
        str(time).translate(translate_text),
        str(date).translate(translate_text),
        namad,
        sod_anbashteh_payan_doreh,
        sod_saham_mosavab_jari,
        sod_anbashteh_payan_doreh_mosavabat,
        sod_khales_har_sahm,
        sod_naghdi_har_sahm,
        sod_anbashted_ebreday_doreh,
        sod_sal_ghabl,
        sahm_1["name"],
        sahm_1["percent"],
        int(sahm_1["sahm"]) * int(sod_naghdi_har_sahm),
        sahm_2["name"],
        sahm_2["percent"],
        int(sahm_2["sahm"]) * int(sod_naghdi_har_sahm),
        sahm_3["name"],
        sahm_3["percent"],
        int(sahm_3["sahm"]) * int(sod_naghdi_har_sahm),
        sahm_4["name"],
        sahm_4["percent"],
        int(sahm_4["sahm"]) * int(sod_naghdi_har_sahm),
        sahm_5["name"],
        sahm_5["percent"],
        int(sahm_5["sahm"]) * int(sod_naghdi_har_sahm),
    )