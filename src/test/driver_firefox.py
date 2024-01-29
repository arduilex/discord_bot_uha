from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# see https://pypi.org/project/webdriver-manager/
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_argument("--headless")
# options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install(), log_output="./selenium.log"))

driver.get("http://google.com")
print("Titre de la page: {}".format(driver.title))
# driver.save_screenshot('screenshot.png')

input("entrez pour quitter")
driver.quit()
