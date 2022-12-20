with open("input.txt", "r") as f:
    data = f.read()

data = [(int(num), i) for i, num in enumerate(data.split("\n"))]

original = data.copy()

for i in range(len(original)):
    idx = data.index(original[i])
    data.pop(idx)
    data.insert((idx + original[i][0]) % len(data), original[i])

for idx, p in enumerate(data):
    if p[0] == 0:
        break

total = 0
for offset in [1000, 2000, 3000]:
    total += data[(idx + offset) % len(data)][0]
print(total)
