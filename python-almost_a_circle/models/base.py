#!/usr/bin/python3
"""Module pour la classe Base"""

class Base:
    """Classe de base pour gérer l'attribut id"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialise une instance de Base avec un id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

