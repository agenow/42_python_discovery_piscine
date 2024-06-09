#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
    raise SystemExit # @tischmid recs this variation, because of version compatibility

for i in range(0, 11):
    print("mult table for", i, end=": ")
    for j in range(0, 11):
        print(i*j, end=" ")
    print()
