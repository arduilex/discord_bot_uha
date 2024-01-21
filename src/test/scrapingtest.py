from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
import time, logging


class Scraping():
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        chrome_service = Service('/usr/lib/chromium-browser/chromedriver')
        self.driver = webdriver.Chrome(service=chrome_service, options=options)
    
    def get_day_menu(self):
        menu_dict = {
            "date": "",
            "menu": []
        }
        try:
            menu_obj = self.driver.find_elements(By.XPATH, "//*[@class='menu slick-slide slick-current slick-active']")
            menu_str = menu_obj[0].text
            menu_dict["date"], *menu_dict["menu"] = menu_str.split('\n')
        except:
            logging.error("Impossible de récupérer le menu")
        return menu_dict

    def get_crous(self):
        self.driver.get("https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2/")
        # enleve le pop up RGPD
        cookie = self.driver.find_element(By.ID, "tru_deselect_btn")
        cookie.click()
        today_date = datetime.now().strftime("%-d")
        next_day_button = self.driver.find_element(By.CLASS_NAME, "next")
        menu_dict = self.get_day_menu()
        if not today_date in menu_dict["date"]:
            next_day_button.click()
            time.sleep(1)
            menu_dict = self.get_day_menu()
        with open("temp/raw_menu.txt", 'w', encoding='utf-8') as file:
                file.write("\n".join(menu_dict["menu"]))

crous = Scraping()
crous.get_crous()