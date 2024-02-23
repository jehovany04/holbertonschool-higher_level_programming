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

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def validate_positive_integer(self, name, value):
        """Validate that value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_non_negative_integer(self, name, value):
        """Validate that value is a non-negative integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

