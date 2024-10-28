# you have to put this file in src/ direcotry
from scraping.crous import CrousScrap
import database.crous as bdd
import os, logging

logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(filename="crous.log",
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        filemode='a')
scrap = CrousScrap()
scrap.get_crous()
bdd.create_menu()
