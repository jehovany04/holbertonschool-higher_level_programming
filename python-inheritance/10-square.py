#!/usr/bin/python3
""" Base Geometry """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Base Geometry """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
