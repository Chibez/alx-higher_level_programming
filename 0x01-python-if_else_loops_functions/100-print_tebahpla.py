#!/usr/bin/python3

for char in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(char)}{chr(char - 32)}", end="")

print()
