#!/usr/bin/python
import sys

count = 0
lines = []
for line in sys.stdin:
    count += 1
    lines.append(line)
    if count == 45:
        with open('output', 'w') as f:
            f.writelines(lines)
        count = 0
        lines = []

    