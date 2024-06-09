#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2 or len(re.findall("z", sys.argv[1])) < 1:
    print("none")
else:
    print(*re.findall("z", sys.argv[1]), sep="")
