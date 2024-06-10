#!/usr/bin/env python3
try:
    num = int(input("Enter a number\n"))
    for i in range (0, 10):
        print(i, "x", num, "=", i*num)
except ValueError:
    print("Number!")
