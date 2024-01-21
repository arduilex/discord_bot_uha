import scraping.crous
from database.crous import CrousBDD
from datetime import datetime
import logging, time, socket, os, schedule
from dotenv import load_dotenv

def send_bot(message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(message.encode())
            s.close()
    except:
        logging.error('Fail to send socket message !')

def check_crous():
    if datetime.today().isoweekday() < 6:
        scraping.crous.get_crous()
        if not crous_bdd.is_closed():
            print("création du menu")
            crous_bdd.create_menu()
            send_bot("menu")

def planificateur():
    schedule.every().day.at("08:00").do(check_crous)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    load_dotenv()
    HOST = str(os.getenv('HOST'))
    PORT = int(os.getenv('PORT'))
    logging.basicConfig(filename="selenium.log",
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        filemode='w')
    crous_bdd = CrousBDD()
    logging.info('main_crous.py Ready to go !')
    # démérrage de la boucle infini, prions qu'elle ne plante jamais :')
    planificateur()
