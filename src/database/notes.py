import json, logging

class NotesBDD():
    def __init__(self):
        self.old_bdd = self.open_notes()
        self.now_bdd = []
        self.new_notes = []

    def open_notes(self):   # return notes in a clean dict
        # read json file and extract title and note
        with open("data/data.json", encoding='utf-8') as json_file:
            try:
                return json.load(json_file)
            except:
                logging.error("Erreur lors de l'extraction des notes")

    def find_new_note(self):
        self.new_notes = []
        if len(self.now_bdd) > len(self.old_bdd):
            for evaluation in self.now_bdd:
                if evaluation not in self.old_bdd:
                    logging.info(f"Nouvelle note détecté en {evaluation['EC']}")
                    self.new_notes.append(evaluation)
            self.old_bdd = self.now_bdd

    def check_new_note(self):
        input()
        self.now_bdd = self.open_notes()
        self.find_new_note()
        if self.new_notes:
            with open("data/new_notes.json", "w", encoding='utf-8') as save:
                json.dump(self.new_notes, save, indent=3, ensure_ascii=False)
            return True
        else:
            return False
