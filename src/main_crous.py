from scraping.crous import CrousScrap
import database.crous as bdd
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
        scrap.get_crous()
        if not bdd.is_closed():
            bdd.create_menu()
            send_bot("menu")

def planificateur():
    schedule.every().day.at("08:31").do(check_crous)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    load_dotenv()
    HOST = str(os.getenv('HOST'))
    PORT = int(os.getenv('PORT'))
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(filename="crous.log",
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        filemode='a')
    scrap = CrousScrap()
    logging.info('Lancement de la planification main_crous.py !')
    # démérrage de la boucle infini, prions qu'elle ne plante jamais :')
    planificateur()
