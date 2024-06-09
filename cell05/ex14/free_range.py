#!/usr/bin/env python3

import sys

print("none" if len(sys.argv) != 3 else [i for i in range(int(sys.argv[1]), int(sys.argv[2])+1)] if int(sys.argv[1]) <= int(sys.argv[2]) else [i for i in range(int(sys.argv[2]), int(sys.argv[1])+1)])
