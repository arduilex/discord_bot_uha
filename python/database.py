import json, logging

class Database():
    def __init__(self):
        self.notes_iut = []
        self.extract()
        self.code_note = self.generate_code_note()
    def extract(self):
        self.notes_iut = []
        # read json file and extract title and note 
        with open("data.json") as json_file:
            data = json.load(json_file)["relevé"]
            ressources = data["ressources"]
            for key_ressources in ressources.keys():
                actual_ressource = ressources[key_ressources]
                self.notes_iut.append({})
                self.notes_iut[-1]["matiere"] = actual_ressource["titre"]
                self.notes_iut[-1]["evaluations"] = []
                for note in actual_ressource["evaluations"]:
                    self.notes_iut[-1]["evaluations"].append({})
                    evaluation = self.notes_iut[-1]["evaluations"][-1]
                    evaluation["titre"] = note["description"]
                    evaluation["date"] = note["date"]
                    evaluation["coef"] = note["coef"]
                    evaluation["note"] = note["note"]
        with open("student.json", "w") as save:
                json.dump(self.notes_iut, save, indent=3, ensure_ascii=False)
    def generate_code_note(self):
        code_note = []
        for matiere in self.notes_iut:
            code_note.append(len(matiere["evaluations"]))
        return code_note
    def check_new_note(self):
        self.extract()
        now_code_note = self.generate_code_note()
        logging.warning(now_code_note)
        if now_code_note != self.code_note:
            self.get_new_note(now_code_note)
            return True
        else:
            return False
    def get_new_note(self, code_note):
        index = None
        number = None
        for i, n in enumerate(zip(self.code_note, code_note)):
            if n[0] != n[1]:
                index = i
                number = abs(n[0]-n[1])
        if index != None:
            write_note = []
            for i in range(1, number+1):
                write_note.append({
                    "matiere": self.notes_iut[index]["matiere"],
                    "evaluation": self.notes_iut[index]["evaluations"][-i]
                    })
            logging.warning(str(number)+" nouvelle(s) note !!! ")
            with open("new_note.json", "w") as save:
                    json.dump(write_note, save, indent=2, ensure_ascii=False)
        self.code_note = code_note