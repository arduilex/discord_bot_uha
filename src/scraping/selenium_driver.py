from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# see https://pypi.org/project/webdriver-manager/

## If you use chromium
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

## If you use firefox
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager

def driver_on():
    options = Options()
    options.add_argument("--headless")
    ## If you use chromium
    return webdriver.Chrome(options=options, service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

    ## If you use firefox
    # return webdriver.Chrome(options=options, service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
