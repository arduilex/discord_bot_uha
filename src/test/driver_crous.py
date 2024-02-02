from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import pickle

# see https://pypi.org/project/webdriver-manager/
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install(), log_output="./selenium.log"))

driver.get("https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2/")

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()


print("Titre de la page: {}".format(driver.title))
# driver.save_screenshot('screenshot.png')

input("entrez pour quitter")

pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

driver.quit()
