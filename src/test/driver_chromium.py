from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# see https://pypi.org/project/webdriver-manager/
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

options = Options()
options.add_argument("--headless")
# options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options, service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("http://google.com")
print("Titre de la page: {}".format(driver.title))
# driver.save_screenshot('screenshot.png')

input("entrez pour quitter")
driver.quit()
