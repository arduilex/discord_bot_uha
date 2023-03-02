from scraping import Scraping
from database import Database
from time import sleep
from os import system
import logging

if __name__ == "__main__":
    logging.basicConfig(filename="scraping.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logging.warning('This will get logged to a file')
    myScraping = Scraping(semestre=2)
    myScraping.get_data()  # pour init le data.json
    myDatabse = Database()
    while 1:
        myScraping.get_data()
        if myDatabse.check_new_note():
            # SEND DISCORD BOT MESSAGE !!
            system('npm start')
        sleep(30)