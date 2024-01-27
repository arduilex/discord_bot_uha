# you have to put this file in src/ direcotry
import scraping.crous as scrap
import database.crous as bdd
import os, logging

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(filename="crous.log",
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        filemode='a')
scrap.get_crous()
bdd.create_menu()
