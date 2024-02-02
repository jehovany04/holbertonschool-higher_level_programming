#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return ''
    else:
        return ''.join([v for v in my_string if v not in 'cC'])
