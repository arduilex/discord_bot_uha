import json, logging

class CrousBDD():
    def __init__(self):
        self.menus = {
            "Déjeuner":[],
            "Menu étudiant 3.30€ ou 1€": [],
            "Menu étudiant végétarien": [],
            "Sandwichs et Salades": [],
            "Sandwichs":[],
            "Salades":[],
            "Pasta Box": [],
            "Origines de nos viandes du jour": []
        }

    def create_menu(self):
        new_menus = self.menus
        with open("temp/raw_menu.txt", 'r', encoding='utf-8') as file:
            current_menu = None
            try:
                for line in file:
                    line = line.strip()
                    if line in new_menus:
                        current_menu = line
                    elif current_menu is not None:
                        new_menus[current_menu].append(line)
            except:
                logging.error("erreur lors de l'extraction du menu raw")
        # supression de ce que je ne veux pas voir
        for key in list(new_menus.keys()):
            if not new_menus[key]:
                del new_menus[key]
        if new_menus["Origines de nos viandes du jour"]:
            del new_menus["Origines de nos viandes du jour"]
        new_menus = {"Menu étudiant" if k == "Menu étudiant 3.30€ ou 1€" else k:v for k,v in new_menus.items()}
        with open('data/menus.json', 'w', encoding='utf-8') as file:
            json.dump(new_menus, file, ensure_ascii=False, indent=4)

    def is_closed(self):
        with open("temp/raw_menu.txt", 'r', encoding='utf-8') as file:
            if len(file.readlines()) < 4:
                return True
            else:
                return False