#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    return [not (v & 1) for v in my_list]
