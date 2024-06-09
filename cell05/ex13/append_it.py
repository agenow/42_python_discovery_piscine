#!/usr/bin/env python3

import sys
import re

print("none" if len(sys.argv) < 2 else *[s+"ism" for s in sys.argv[1:] if not re.search(r"ism$", s)]), sep="\n")

#for s in sys.argv[1:]:
#    if not re.search(r"ism$", s):
#        print(s+"ism")
