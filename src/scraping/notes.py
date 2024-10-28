from .selenium_driver_raspi import driver_on
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os, logging, json, requests

class NotesScrap():
    def __init__(self):
        load_dotenv()
        self.etudiant_id = {
            "email"   : os.getenv('email'),
            "password": os.getenv('password')
        }

    def get_notes(self):
        driver = driver_on()
        try:
            # login into icam cas
            logging.info("Connexion icam en cours...")
            driver.get("https://planning.icam.fr/")
            ident = driver.find_element(By.ID, "username")
            ident.send_keys(self.etudiant_id["email"])
            psw = driver.find_element(By.ID, "password")
            psw.send_keys(self.etudiant_id["password"])
            button_login = driver.find_element(By.ID, "hyperplanningSubmitBtn")
            button_login.click()
        except:
            logging.error("Impossible de se connecter Icam cas")
        try:
            # find notes
            dernieres_notes = "//header[@title='Les 10 dernières notes']"
            WebDriverWait(driver, 10).until(lambda driver_: driver_.find_element(By.XPATH, dernieres_notes))
            driver.find_element(By.XPATH, dernieres_notes).click()
            WebDriverWait(driver, 10).until(lambda driver_: driver_.find_elements(By.CLASS_NAME, "ie-titre-gros"))
            raw_notes = []
            for data in driver.find_elements(By.CLASS_NAME, "infos-supp"):
                data.click()
                detail_note = driver.find_elements(By.CLASS_NAME, "Zone-DetailsNotes")
                raw_notes.append(detail_note[0].text.split("\n"))
            driver.quit()
        except:
            logging.error("impossible de récupérer les notes")
        self.save_notes(raw_notes)

    def save_notes(self, data):
        try:
            list_notes = []
            for e in data:
                list_notes.append({
                    "EC":e[0],
                    "titre": e[1],
                    "date": e[2][8:],
                    "moy": e[6],
                    "max": e[8],
                    "min": e[10],
                    "coef": e[12],
                    "base": e[13]
                    })
            json_notes = json.dumps(list_notes, indent=4, ensure_ascii=False)
            with open("data/data.json", 'w', encoding='utf-8') as json_file:
                json_file.write(json_notes)
        except:
            logging.error("erreur lors de l'extraction de note")
