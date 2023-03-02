from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json, os, dotenv, time, logging

class Scraping():
    def __init__(self, semestre):
        # pour request la 
        semestre_code = {
            1:"192",
            2:"425",
            3:"449",
            4:"494"
        }
        dotenv.load_dotenv()
        self.email = os.getenv('email')
        self.password = os.getenv('password')
        self.semestre_acces = semestre_code[semestre]
        options = Options()
        # options.add_argument("start-maximized")  
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def login(self):
        self.driver.get("https://cas.uha.fr/cas/login")
        ident = self.driver.find_element(By.ID, "username")
        ident.send_keys(self.email)
        psw = self.driver.find_element(By.ID, "password")
        psw.send_keys(self.password)
        login = self.driver.find_element(By.NAME, "submit")
        login.click()
        self.driver.get("https://notes.iutmulhouse.uha.fr/")

    def get_data(self):
        try: 
            self.driver.get("https://notes.iutmulhouse.uha.fr/services/data.php?q=relev%C3%A9Etudiant&semestre="+self.semestre_acces)
            text_file = self.driver.page_source
            if "redirect" in text_file:
                logging.warning("error, login again !")
                self.login()
                self.get_data()
            else:
                logging.warning("get data")
                with open("data.json", "w", encoding='utf-8') as save:
                    json.dump(json.loads(text_file[131:-20]), save, indent=2, ensure_ascii=False)
        except:
            logging.warning("error network, try in 10 sec")
            time.sleep(10)
            self.get_data()