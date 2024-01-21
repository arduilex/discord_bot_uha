# you have to put tjis file in src/ direcotry
import scraping.notes
from database.notes import NotesBDD

scraping.notes.get_notes()
notes_bdd = NotesBDD()