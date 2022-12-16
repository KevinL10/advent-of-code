with open("input.txt", "r") as f:
    data = f.read()

data = [list(map(int, l)) for l in data.split("\n")]
total = 0

rows = len(data)
cols = len(data[0])

for r in range(rows):
    for c in range(cols):

        up = all([data[i][c] < data[r][c] for i in range(r)])
        down = all([data[i][c] < data[r][c] for i in range(r + 1, rows)])
        left = all([data[r][i] < data[r][c] for i in range(c)])
        right = all([data[r][i] < data[r][c] for i in range(c + 1, cols)])

        if left or right or up or down:
            total += 1

print(total)
