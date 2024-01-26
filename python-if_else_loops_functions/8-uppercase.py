#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            c = chr(ord(str[i]) - 32)
        else:
            c = str[i]
        print("{:s}".format(c), end="")
    print("")
