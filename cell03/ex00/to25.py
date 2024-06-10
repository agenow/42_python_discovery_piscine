#!/usr/bin/env python3

import sys

num = int(input())
if num > 25: sys.exit("Error")
for num in range(num, 26):
    print("~", num)

