from .selenium_driver import driver_on
from selenium.webdriver.common.by import By
from datetime import datetime
import logging, time, pickle

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
        driver.get("https://www.crous-strasbourg.fr/restaurant/resto-u-de-liut-mulhouse-2/")
        logging.info("crous access")
        # Add cookie to skip popup
        cookies = pickle.load(open("data/cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        today_date = datetime.now().strftime("%-d")
        next_day_button = driver.find_element(By.CLASS_NAME, "next")
        menu_dict = get_day_menu(driver)
        if not today_date in menu_dict["date"]:
            next_day_button.click()
            time.sleep(2)
            menu_dict = get_day_menu(driver)
        with open("data/raw_menu.txt", "w", encoding='utf-8') as file:
            file.write("\n".join(menu_dict["menu"]))
        logging.info(f"{menu_dict['date']} trouvé !")
        driver.quit()
    except:
        logging.error("Impossible d'accéder au site crous")
        driver.quit()
        time.sleep(5)
        get_crous()
