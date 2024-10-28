import json, logging

def create_menu():
    new_menus = {
        "Déjeuner":[],
        "Grillade": [],
        "Plat du jour": [],
        "Végétarien": [],
        "Extension":[],
    }
    try:
        with open("data/raw_menu.txt", encoding='utf-8') as file:
            current_menu = None
            for line in file:
                line = line.strip()
                if line in new_menus:
                    current_menu = line
                elif current_menu is not None:
                    new_menus[current_menu].append(line)
        # supression des clés vides
        for key in list(new_menus.keys()):
            if not new_menus[key]:
                del new_menus[key]
        with open('data/menus.json', "w", encoding='utf-8') as file:
            json.dump(new_menus, file, ensure_ascii=False, indent=4)
        logging.info("menu du crous json créé !")
    except Exception as e:
        logging.error("erreur lors de l'extraction du menu raw", e)


def is_closed():
    with open("data/raw_menu.txt") as file:
        if len(file.readlines()) < 4:
            return True
        else:
            return False
