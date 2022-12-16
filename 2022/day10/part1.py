with open("input.txt", "r") as f:
    data = f.read()

cycle = 1
X = 1
total = 0

for line in data.split("\n"):
    cycle += 1
    if cycle % 40 == 20:
        total += cycle * X

    if "noop" in line:
        continue

    cycle += 1
    value = int(line.split(" ")[1])
    X += value

    if cycle % 40 == 20:
        total += cycle * X

print(total)
