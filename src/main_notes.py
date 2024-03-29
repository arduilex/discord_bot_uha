from database.notes import NotesBDD
from scraping.notes import NotesScrap
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
    scrap.get_notes()
    if bdd.check_new_note():
        send_bot("notes")

def planificateur():
    schedule.every(1).minutes.do(check_notes)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    load_dotenv()
    HOST = str(os.getenv('HOST'))
    PORT = int(os.getenv('PORT'))
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(filename="notes.log",
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        filemode='a')

    scrap = NotesScrap()
    bdd = NotesBDD()
    logging.info('Lancement de la plannification "notes"')
    # démérrage de la boucle infini, prions qu'elle ne plante jamais :')
    planificateur()
