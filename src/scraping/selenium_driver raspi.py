from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def driver_on():
    options = Options()
    # options.add_argument('--headless')
    # see https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi
    chrome_service = Service('/usr/bin/chromedriver')
    return webdriver.Chrome(service=chrome_service, options=options)
