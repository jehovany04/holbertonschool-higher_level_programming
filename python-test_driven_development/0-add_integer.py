#!/usr/bin/python3
"""Module for add_integer function."""


def add_integer(a, b=98):
    """
    Description:
        Function that adds 2 integers.
        If a or b is a float, it should be casted to an integer.

    Args:
        a = int
        b = int

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        The sum of a and b (int)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

