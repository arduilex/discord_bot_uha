# you have to put tjis file in src/ direcotry
import scraping.crous
from database.crous import CrousBDD
import os

os.makedirs("temp", exist_ok=True)
os.makedirs("data", exist_ok=True)
crous_bdd = CrousBDD()
scraping.crous.get_crous()
crous_bdd.create_menu()