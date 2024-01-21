from .selenium_driver import driver_on
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os, logging, json

def notes_login():
    try:
        driver.get("https://cas.uha.fr/cas/login")
        ident = driver.find_element(By.ID, "username")
        ident.send_keys(email)
        psw = driver.find_element(By.ID, "password")
        psw.send_keys(password)
        button_login = driver.find_element(By.NAME, "submit")
        button_login.click()
        driver.save_screenshot('screenshot.png')
        driver.get("https://notes.iutmulhouse.uha.fr/")
    except:
        logging.error("Impossible de se connecter uha")

def get_notes():
    try:
        driver.get(
            "https://notes.iutmulhouse.uha.fr/services/data.php?q=relev%C3%A9Etudiant&semestre="+semestre_acces)
        text_file = driver.page_source
        if ("redirect" in text_file) or ("erreur" in text_file):
            logging.warning("no login !")
            notes_login()
            get_notes()
        else:
            with open("temp/data.json", "w", encoding='utf-8') as save:
                json.dump(json.loads(text_file[131:-20]), save, indent=2, ensure_ascii=False)
    except:
        logging.error("Impossible de récupérer la note")

#init
semestre = 5
semestre_code = {
    1: "192",
    2: "425",
    3: "449",
    4: "494",
    5: "530"
}
load_dotenv()
email = os.getenv('email')
password = os.getenv('password')
php_request = os.getenv('php_request')
semestre_acces = php_request
driver = driver_on()
notes_login()