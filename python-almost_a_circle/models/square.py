#!/usr/bin/python3
"""Module for the Square class"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.validate_positive_integer("size", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes"""

        if len(args) > 0:
            self.id = args[0]
        elif kwargs.get('id') is not None:
            self.id = kwargs['id']

        if len(args) > 1:
            self.size = args[1]
        elif kwargs.get('size') is not None:
            self.size = kwargs['size']

        if len(args) > 2:
            self.x = args[2]
        elif kwargs.get('x') is not None:
            self.x = kwargs['x']

        if len(args) > 3:
            self.y = args[3]
        elif kwargs.get('y') is not None:
            self.y = kwargs['y']

    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

