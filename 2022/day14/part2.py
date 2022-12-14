with open("input.txt", "r") as f:
    data = f.read()

SZ = 1000
grid = [["."] * SZ for _ in range(SZ)]
depth = 0

for line in data.strip().split("\n"):
    pairs = [list(map(int, p.split(","))) for p in line.split("->")]
    for p1, p2 in zip(pairs, pairs[1:]):
        p1 = p1[:]
        p2 = p2[:]

        p1[0], p2[0] = sorted([p1[0], p2[0]])
        p1[1], p2[1] = sorted([p1[1], p2[1]])

        for r in range(p1[0], p2[0] + 1):
            for c in range(p1[1], p2[1] + 1):
                grid[r][c] = "#"

        depth = max(depth, p2[1])

count = 0

for i in range(SZ):
    grid[i][depth + 2] = "#"

while grid[500][0] == ".":
    x = 500
    y = 0
    while True:
        if grid[x][y + 1] == ".":
            y += 1
        elif grid[x - 1][y + 1] == ".":
            x -= 1
            y += 1
        elif grid[x + 1][y + 1] == ".":
            x += 1
            y += 1
        else:
            grid[x][y] = "o"
            break

    count += 1

print(count)
