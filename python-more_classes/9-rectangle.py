#!/usr/bin/python3
""" rectangle """


class Rectangle():
    """ rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        w, h = self.width, self.height
        return w * h

    def perimeter(self):
        w, h = self.width, self.height
        if w == 0 or h == 0:
            return 0
        return w * 2 + h * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''
        return '\n'.join([str(self.print_symbol) * self.width
                          for _ in range(self.height)])

    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) not in [Rectangle]:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) not in [Rectangle]:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2

        return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
