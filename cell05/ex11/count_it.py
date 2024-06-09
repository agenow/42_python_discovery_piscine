#!/usr/bin/env python3

import sys

sys.exit("none") if len(sys.argv) < 2 else print("params:", len(sys.argv[1:]))
for a in sys.argv[1:]:
    print("%s: %i" % (a, len(a)))
