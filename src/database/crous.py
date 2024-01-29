import json, logging

def create_menu():
    new_menus = {
        "Déjeuner":[],
        "Menu étudiant 3.30€ ou 1€": [],
        "Menu étudiant végétarien": [],
        "Sandwichs et Salades": [],
        "Sandwichs":[],
        "Salades":[],
        "Pasta Box": [],
        "Origines de nos viandes du jour": []
    }
    with open("data/raw_menu.txt", encoding='utf-8') as file:
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
    # supression des clés vides
    for key in list(new_menus.keys()):
        if not new_menus[key]:
            del new_menus[key]
    if new_menus["Origines de nos viandes du jour"]:
        del new_menus["Origines de nos viandes du jour"]
    with open('data/menus.json', "w", encoding='utf-8') as file:
        json.dump(new_menus, file, ensure_ascii=False, indent=4)

def is_closed():
    with open("data/raw_menu.txt", encoding='utf-8') as file:
        if len(file.readlines()) < 4:
            return True
        else:
            return False
