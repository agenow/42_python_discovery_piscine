#!/usr/bin/env python3

import sys

def downcase_it(s:str): return s.lower()
print("none") if len(sys.argv) < 2 else [print(downcase_it(i)) for i in sys.argv[1:]]
