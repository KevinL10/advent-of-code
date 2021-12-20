with open('input.txt') as f:
	lines = f.read().splitlines()

enhancement = lines[0]
lines = lines[2:]

row = len(lines)
col = len(lines[0])

SIZE = 600

out = [['.' for i in range(SIZE)] for i in range(SIZE)]

for i in range(row):
	for a in range(col):
		out[i + SIZE // 2][a + SIZE // 2] = lines[i][a]

lines = [row[:] for row in out]

curmin = 1
curmax = SIZE - 1
for steps in range(50):
	for i in range(curmin, curmax):
		for a in range(curmin, curmax):
			others = ''
			for xi in range(-1, 2):
				for xa in range(-1, 2):
					newi = i + xi
					newa = a + xa
					if lines[newi][newa] == '.':
						others += '0'
					else:
						others += '1'
			others = int(others, 2)
			out[i][a] = enhancement[others]

	lines = [row[:] for row in out]
	curmin += 1
	curmax -= 1

cnt = 0
for i in range(curmin, curmax):
	for a in range(curmin, curmax):
		if lines[i][a] == '#':
			cnt += 1

print(cnt)