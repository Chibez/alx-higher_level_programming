#!/usr/bin/python3

def uppercase(input_str):
    for char in input_str:
        if 'a' <= char <= 'z':
            char = char.upper()
        print(char, end="")
    print()
