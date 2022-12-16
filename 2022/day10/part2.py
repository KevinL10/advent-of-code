with open("input.txt", "r") as f:
    data = f.read()

cycle = 0
X = 1
img = [["."] * 40 for _ in range(6)]

for line in data.split("\n"):
    if cycle % 40 in [X - 1, X, X + 1]:
        img[cycle // 40][cycle % 40] = "#"

    cycle += 1
    if "noop" in line:
        continue

    if cycle % 40 in [X - 1, X, X + 1]:
        img[cycle // 40][cycle % 40] = "#"

    cycle += 1
    value = int(line.split(" ")[1])
    X += value


print("\n".join(["".join(l) for l in img]))
