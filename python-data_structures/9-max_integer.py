#!/usr/bin/python3


def max_integer(my_list=[]):
    return {i: v for i, v
            in enumerate(sorted(my_list, reverse=True))}.get(0, None)
