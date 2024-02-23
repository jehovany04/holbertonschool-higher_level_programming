#!/usr/bin/python3
"""Module for the Square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance"""

        super().__init__(size, size, x, y, id)  # Call the constructor of the Rectangle class

    # ... (rest of the code)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.width,  # Since width and height are the same in a Square
            'x': self.x,
            'y': self.y
        }

