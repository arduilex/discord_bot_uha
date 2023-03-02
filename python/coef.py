import json

notes_iut = []
# read json file and extract title and note 
with open("data.json") as json_file:
    data = json.load(json_file)["relevé"]
    ressources = data["ressources"]
    for key_ressources in ressources.keys():
        actual_ressource = ressources[key_ressources]
        notes_iut.append({})
        notes_iut[-1]["matiere"] = actual_ressource["titre"]
        notes_iut[-1]["evaluations"] = []
        for note in actual_ressource["evaluations"]:
            notes_iut[-1]["evaluations"].append({})
            evaluation = notes_iut[-1]["evaluations"][-1]
            evaluation["titre"] = note["description"]
            evaluation["date"] = note["date"]
            evaluation["coef"] = note["coef"]
            evaluation["moyenne"] = note["note"]["moy"]
with open("student.json", "w") as save:
        json.dump(notes_iut, save, indent=3, ensure_ascii=False)