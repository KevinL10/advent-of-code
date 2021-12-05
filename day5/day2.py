with open('input.txt') as f:
	lines = f.read().splitlines()

def sign(x):
	if x >= 0:
		return 1
	return -1

size = 1000
overlaps = [[0] * size for i in range(size)]

for line in lines:
	start, end = line.split(' -> ')
	x1, y1 = list(map(int, start.split(',')))
	x2, y2 = list(map(int, end.split(',')))

	if x1 == x2:
		if y1 > y2:
			y1, y2 = y2, y1
		for y in range(y1, y2 + 1):
			overlaps[x1][y] += 1
	elif y1 == y2:
		if x1 > x2:
			x1, x2 = x2, x1
		for x in range(x1, x2 + 1):
			overlaps[x][y1] += 1
	else:
		dirx = sign(x2 - x1)
		diry = sign(y2 - y1)

		for i in range(abs(x2 - x1) + 1):
			overlaps[x1 + dirx * i][y1 + diry * i] += 1


cnt = 0

for i in range(size):
	for a in range(size):
		if overlaps[i][a] >= 2:
			cnt += 1

print(cnt)
