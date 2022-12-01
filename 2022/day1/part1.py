from collections import defaultdict
import sys


data = open("input.txt").read()


cmax = 0
s = 0
for l in data.split("\n"):
    if len(l) == 0:
        s = 0
    else:
        s += int(l)
    
    cmax = max(cmax, s)


print(cmax)