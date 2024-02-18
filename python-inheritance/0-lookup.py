#!/usr/bin/python3
"""
    retrieve the list of attributes and methods available in a given object.
"""


def lookup(obj):
    """
    obtain the list of attributes and methods of a specified object.
    """
    return dir(obj)
