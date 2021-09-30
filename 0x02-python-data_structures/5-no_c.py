#!/usr/bin/python3
def no_c(my_string):
    noc_str = ''.join(char for char in my_string if char not in 'Cc')
    return noc_str
