from collections import defaultdict
import sys

data = open("input.txt").read()


sums = []
s = 0
for l in data.split("\n"):
    if len(l) == 0:
        sums.append(s)
        s = 0
    else:
        s += int(l)
    

sums.append(s)
sums.sort()
print(sums[-1] + sums[-2] + sums[-3])