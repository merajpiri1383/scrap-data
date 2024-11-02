from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.headless = True

prefs = {
    "profile.managed_default_content_settings.images" : 2 ,
    "profile.managed_default_content_settings.stylesheets" : 2
}

chrome_options.add_experimental_option("prefs",prefs)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")