#!/usr/bin/python3
""" inherits from """


def inherits_from(obj, a_class):
    """ inherits from """
    return type(obj) is not a_class and isinstance(obj, a_class)
