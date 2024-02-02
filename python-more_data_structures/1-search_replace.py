#!/usr/bin/python3

def search_replace(my_list, search, replace):
    my_list_result = my_list[:]
    for i in range(len(my_list_result)):
        if search == my_list_result[i]:
            my_list_result[i] = replace
    return my_list_result
