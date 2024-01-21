from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# Vous pouvez ajouter des options spécifiques ici si nécessaire
# Par exemple: options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor='http://172.17.0.2:4444/wd/hub',
    options=options)

driver.get("http://google.com")
print("Titre de la page: ", driver.title)

# driver.save_screenshot('screenshot.png')
input()
driver.quit()
