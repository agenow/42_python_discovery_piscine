#!/usr/bin/env python3

import sys

print("none") if len(sys.argv) < 2 else print(*reversed(sys.argv[1:]), sep="\n")
