from .selenium_driver import driver_on
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os, logging, json, requests

class NotesScrap():
    def __init__(self):
        load_dotenv()
        self.etudiant_id = {
            "email"   : os.getenv('email'),
            "password": os.getenv('password')
        }
        self.php_id = {
            "semestre": os.getenv('php_request'),
            "sess_id" : ""
        }

    def generate_token(self):
        try:
            driver = driver_on()
            logging.info("Connexion uha en cours...")
            driver.get("https://cas.uha.fr/cas/login")
            ident = driver.find_element(By.ID, "username")
            ident.send_keys(self.etudiant_id["email"])
            psw = driver.find_element(By.ID, "password")
            psw.send_keys(self.etudiant_id["password"])
            button_login = driver.find_element(By.NAME, "submit")
            button_login.click()
            driver.get("https://notes.iutmulhouse.uha.fr/")
            logging.info("Connexion uha résussis !")
            cookie = driver.get_cookies()
            new_php_id = cookie[0]["value"]
            driver.quit()
            self.php_id["sess_id"] = new_php_id
        except:
            logging.error("Impossible de récupérer le token")

    def get_notes(self):
        try:
            url = 'https://notes.iutmulhouse.uha.fr/services/data.php'
            cookies = {'PHPSESSID': self.php_id["sess_id"]}
            params = {'q': 'relevéEtudiant', 'semestre': self.php_id["semestre"]}
            r = requests.post(url, cookies=cookies, params=params)
            if "doAuth" in r.text:
                logging.warning("miss login !")
                self.generate_token()
                self.get_notes()
            else:
                with open("data/data.json", 'w', encoding='utf-8') as file:
                    json.dump(r.json(), file, indent=2, ensure_ascii=False)
        except:
            logging.error("Impossible de récupérer la note")

