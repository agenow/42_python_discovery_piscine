#!/usr/bin/env python3

import sys

def shrink(s:str): return (s[:8])
def enlarge(s:str): return s+'Z'

if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        while len(arg) < 8: arg=enlarge(arg)
        if len(arg) > 8: arg=shrink(arg)
        print(arg)
