from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
options.add_argument("--headless")  # Assurez-vous d'utiliser deux tirets
# options.add_argument("--disable-gpu")

# see https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi
chrome_service = Service('/usr/lib/chromium-browser/chromedriver')

# Initialisez le WebDriver avec les options et le service spécifiés
chrome = webdriver.Chrome(service=chrome_service, options=options)

chrome.get("http://apple.com")

print("Titre de la page: {}".format(chrome.title))
# chrome.save_screenshot('screenshot.png')

input("entrez pour quitter")

chrome.quit()
