import scraping.notes
from database.notes import NotesBDD
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

def check_notes():
    scraping.notes.get_notes()
    if notes_bdd.check_new_note():
        send_bot("notes")

def planificateur():
    schedule.every(10).minutes.do(check_notes)
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
    scraping.notes.get_notes()
    notes_bdd = NotesBDD()
    logging.info('main_notes.py Ready to go !')
    # démérrage de la boucle infini, prions qu'elle ne plante jamais :')
    planificateur()

