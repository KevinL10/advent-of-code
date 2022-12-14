with open("input.txt", "r") as f:
    data = f.read()

grid = [["."] * 1000 for i in range(1000)]
depth = 0

for line in data.split("\n"):
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

while True:
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

        if y == depth + 1:
            print(count)
            exit()

    count += 1
