#!/usr/bin/env python3

import sys
import re

print("none" if len(sys.argv) != 3 else len(re.findall(sys.argv[1], sys.argv[2])))
