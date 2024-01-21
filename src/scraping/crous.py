from .selenium_driver import driver_on
from selenium.webdriver.common.by import By
from datetime import datetime
import logging, time

def skip_cookie(driver):
    driver.get("https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2/")
    cookie = driver.find_element(By.ID, "tru_deselect_btn")
    cookie.click()

def get_day_menu(driver):
    menu_dict = {
        "date": "",
        "menu": []
    }
    try:
        menu_obj = driver.find_elements(By.XPATH, "//*[@class='menu slick-slide slick-current slick-active']")
        menu_str = menu_obj[0].text
        menu_dict["date"], *menu_dict["menu"] = menu_str.split('\n')
    except:
        logging.error("Impossible de récupérer le menu")
    return menu_dict

def get_crous():
    try:
        driver = driver_on()
        skip_cookie(driver)
        driver.get("https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2/")
        today_date = datetime.now().strftime("%-d")
        next_day_button = driver.find_element(By.CLASS_NAME, "next")
        menu_dict = get_day_menu(driver)
        if not today_date in menu_dict["date"]:
            next_day_button.click()
            time.sleep(1)
            menu_dict = get_day_menu(driver)
        with open("temp/raw_menu.txt", "w", encoding='utf-8') as file:
                file.write("\n".join(menu_dict["menu"]))
        driver.quit()
    except:
        logging.error("Impossible d'accéder au site crous")
