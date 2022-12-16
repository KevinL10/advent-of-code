from collections import defaultdict

with open("input.txt", "r") as f:
    data = f.read()

cwd = []
sizes = defaultdict(int)

for line in data.split("\n"):
    if "$ cd" in line:          # if cd, then update current directory
        _, cmd, dir = line.split(' ')
        if dir == "..":
            cwd = cwd[:-1]
        else:
            cwd.append(dir) 
    
    elif "$ ls" in line:        # if ls, do nothing
        continue
    else:                       
        sz, name = line.split()
        if sz.isnumeric():      # if line contains a filesize, then update current and parent directory sizes
            for i in range(1, len(cwd) + 1):
                sizes['/'.join(cwd[0:i])] += int(sz)

print(sum(filter(lambda x: x < 100000, sizes.values())))