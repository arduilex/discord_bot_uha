# you have to put tjis file in src/ direcotry
from scraping.notes import NotesScrap
from database.notes import NotesBDD


my_scrap = NotesScrap()
my_scrap.get_notes()

