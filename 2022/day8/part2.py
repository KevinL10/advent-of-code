with open("input.txt", "r") as f:
    data = f.read()

data = [list(map(int, l)) for l in data.split("\n")]
score = 0
rows = len(data)
cols = len(data[0])

for r in range(rows):
    for c in range(cols):
        up = down = left = right = 0

        for i in range(r - 1, -1, -1):
            up += 1
            if data[i][c] >= data[r][c]:
                break

        for i in range(r + 1, rows):
            down += 1
            if data[i][c] >= data[r][c]:
                break

        for i in range(c - 1, -1, -1):
            left += 1
            if data[r][i] >= data[r][c]:
                break

        for i in range(c + 1, cols):
            right += 1
            if data[r][i] >= data[r][c]:
                break

        score = max(score, up * down * left * right)

print(score)
