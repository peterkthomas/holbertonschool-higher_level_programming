#!/usr/bin/python3
def search_replace(my_list, search, replace):
    temp_list = my_list.copy()
    for x, i in enumerate(temp_list):
        if i == search:
            temp_list[x] = replace
    return temp_list
