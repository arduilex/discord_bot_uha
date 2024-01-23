# you have to put this file in src/ direcotry
import scraping.crous as scrap
import database.crous as bdd
import os

os.makedirs("temp", exist_ok=True)
os.makedirs("data", exist_ok=True)
scrap.get_crous()
bdd.create_menu()
