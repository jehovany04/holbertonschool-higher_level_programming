# Dans models/rectangle.py

class Rectangle(Base):
    # ... (autres méthodes et propriétés)

    @classmethod
    def create(cls, **dictionary):
        """Crée une instance de Rectangle à partir d'un dictionnaire"""
        new_rect = cls(1, 1)  # Les valeurs par défaut peuvent être modifiées
        new_rect.update(**dictionary)
        return new_rect

