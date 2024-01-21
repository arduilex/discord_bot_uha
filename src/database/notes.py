import json, logging

class NotesBDD():
    def __init__(self):
        self.old_bdd = self.extract()
        self.now_bdd = []
        self.new_notes = []

    def extract(self):   # return notes in a clean dict
        # read json file and extract title and note
        with open("temp/data.json", encoding='utf-8') as json_file:
            try:
                evaluation_bdd = []
                data = json.load(json_file)
                ressources = data["relevé"]["ressources"]
                for ressource in ressources.values():
                    matiere_name = ressource["titre"].split(":")[-1][0:] # supression de R05.4
                    for eval in ressource["evaluations"]:
                        if eval["note"]["value"] != "~":
                            evaluation_bdd.append({})
                            insert = evaluation_bdd[-1]
                            insert["matiere"] = matiere_name
                            insert["titre"] = eval["description"]
                            insert["date"] = eval["date"]
                            insert["coef"] = eval["coef"]
                            insert["note"] = eval["note"]
            except:
                logging.error("Erreur lors de l'extraction des notes")
        # pour marquer en dure la bdd
        with open("temp/evaluation.json", "w", encoding='utf-8') as save:
            json.dump(evaluation_bdd, save, indent=3, ensure_ascii=False)
        return evaluation_bdd

    def find_new_note(self):
        self.new_notes = []
        if len(self.now_bdd) > len(self.old_bdd):
            for evaluation in self.now_bdd:
                if evaluation not in self.old_bdd:
                    logging.info(f"Nouvelle note détecté en {evaluation['matiere']}")
                    self.new_notes.append(evaluation)
            self.old_bdd = self.now_bdd

    def check_new_note(self):
        self.now_bdd = self.extract()
        self.find_new_note()
        if self.new_notes:
            with open("data/new_notes.json", "w", encoding='utf-8') as save:
                json.dump(self.new_notes, save, indent=3, ensure_ascii=False)
            return True
        else:
            return False
