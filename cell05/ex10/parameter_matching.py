#!/usr/bin/env python3

import sys

print("none" if len(sys.argv) != 2 else "Good job!" if input("What was your param? ") == sys.argv[1] else "Nope, sorry...")
