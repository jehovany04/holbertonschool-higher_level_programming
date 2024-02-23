#!/usr/bin/python3
"""Module for the Rectangle class"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance"""

        super().__init__(id)  # Call the constructor of the Base class with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ... (rest of the code)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

