import os 
# os.chdir("../")

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


import pickle

# see https://pypi.org/project/webdriver-manager/
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument("--headless")
# options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install(), log_output="./selenium.log"))

driver.get("https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2/")

print("ouuuuu")
cookies = pickle.load(open("data/cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)

# driver.refresh()


menu_obj = driver.find_elements(By.XPATH, "//*")


with open("data/raw_crous.txt", 'w', encoding='utf-8') as file:
    for menu in menu_obj:
        try:
            file.write(menu.text)
        except:
            continue


driver.quit()
