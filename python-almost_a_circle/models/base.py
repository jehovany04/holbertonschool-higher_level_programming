#!/usr/bin/python3
"""Module pour la classe Base"""

import json

class Base:
    """Classe de base pour toutes les autres classes de ce projet"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise une instance de Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Renvoie la représentation JSON en chaîne de list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Écrit la représentation JSON en chaîne de list_objs dans un fichier"""
        nom_fichier = cls.__name__ + ".json"

        with open(nom_fichier, "w") as fichier:
            if list_objs is None:
                fichier.write("[]")
            else:
                liste_dict = [obj.to_dictionary() for obj in list_objs]
                fichier.write(cls.to_json_string(liste_dict))

    @staticmethod
    def from_json_string(json_string):
        """Renvoie la liste de la représentation JSON en chaîne json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Renvoie une liste d'instances depuis un fichier"""
        nom_fichier = cls.__name__ + ".json"

        try:
            with open(nom_fichier, "r") as fichier:
                contenu = fichier.read()
                liste_dicts = cls.from_json_string(contenu)
                return [cls.create(**item) for item in liste_dicts]
        except FileNotFoundError:
            return []

