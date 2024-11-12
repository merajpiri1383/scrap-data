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
    "سهامدار ۱",
    "درصد مالکیت",
    "مبلغ"
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
        if "جمع" not in row.text : 
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

    sod_table = driver.find_element(By.ID,"ucAssemblyPRetainedEarning_grdAssemblyProportionedRetainedEarning")

    rows_sod_table = sod_table.find_elements(By.XPATH,".//tr")

    sod_naghdi_har_sahm = None
    sod_khales_har_sahm = None
    sod_anbashteh_payan_doreh = None
    sod_saham_mosavab_jari = None
    sod_anbashteh_payan_doreh_mosavabat = None

    if len (rows_sod_table) > 3 : 
        for index,row in enumerate(rows_sod_table) : 
            if "انباشته پايان دوره" in row.text.strip() : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_anbashteh_payan_doreh = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(translate_text)
            if "سود نقدی هر سهم" in row.text.strip() : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_naghdi_has_sahm = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(translate_text)
            
            if "سهام مصوب" in row.text.strip() and "جاری" in row.text.strip() : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_saham_mosavab_jari = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(translate_text)
            
            if "لحاظ نمودن مصوبات مجمع" in row.text.strip() : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_anbashteh_payan_doreh_mosavabat = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(translate_text)

            if "خالص هر سهم" in row.text.strip() : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_khales_har_sahm = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(translate_text)
            
            if "نقدی هر سهم" in row.text.strip() : 
                tds = row.find_elements(By.XPATH,".//td")
                sod_naghdi_har_sahm = str(driver.execute_script("return arguments[0].innerText",tds[2])).translate(translate_text)
    

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
        saham_daran_list[0]["name"],
        saham_daran_list[0]["percent"],
        int(saham_daran_list[0]["sahm"]) * int(sod_naghdi_har_sahm)
    )