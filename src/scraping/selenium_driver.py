from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def driver_on():
    options = Options()
    options.add_argument('--headless')
    chrome_service = Service('/usr/lib/chromium-browser/chromedriver')
    return webdriver.Chrome(service=chrome_service, options=options)
