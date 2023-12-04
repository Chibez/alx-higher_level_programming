#!/usr/bin/env python3

def no_c(my_string):
    resu = ""
    for char in my_string:
        if char.lower() != 'c':
            resu += char
    return resu
