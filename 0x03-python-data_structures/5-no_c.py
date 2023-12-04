#!/usr/bin/python3

def no_c(my_string):
    dated_str = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            updated_str += i
    return (dated_str)
