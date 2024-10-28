# you have to put this file in src/ direcotry
from scraping.notes import NotesScrap
from database.notes import NotesBDD


#my_scrap = NotesScrap()
#my_scrap.get_notes()
my_bdd = NotesBDD()
my_bdd.check_new_note()
