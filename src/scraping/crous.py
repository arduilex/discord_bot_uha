from .selenium_driver import driver_on
from selenium.webdriver.common.by import By
from datetime import datetime
import logging, time, pickle

class CrousScrap():
    def __init__(self):
        self.crous_menu = ""
        self.crous_date = ""

    def get_day_menu(self, driver):
        try:
            menu_obj = driver.find_elements(By.XPATH, "//*[@class='menu slick-slide slick-current slick-active']")
            menu_str = menu_obj[0].text
            self.crous_date, *self.crous_menu = menu_str.split('\n')
        except:
            logging.error("Impossible de récupérer le menu")

    def get_crous(self):
        driver = driver_on()
        # try:
        driver.get("https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse/")
        logging.info("crous website loaded sucessfull")
        # Add cookie to skip popup
        cookies = pickle.load(open("data/cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        today_date_number = datetime.now().strftime("%-d")
        today_date_number = "6"
        self.get_day_menu(driver)
        while not today_date_number in self.crous_date:
            next_day_button = driver.find_element(By.CLASS_NAME, "next")
            next_day_button.click()
            logging.info("clic sur le bouton suivant")
            time.sleep(1)
            self.get_day_menu(driver)
        with open("data/raw_menu.txt", "w", encoding='utf-8') as file:
            file.write("\n".join(self.crous_menu))
        logging.info(f"{self.crous_date} trouvé !")
        driver.quit()
        # except:
        #     logging.error("erreur lors de l'accès au site crous")
        #     driver.quit()
        #     time.sleep(5)
        #     self.get_crous()
