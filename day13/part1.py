with open('input.txt') as f:
	lines = f.read().splitlines()

grid = [[' '] * 2000 for _ in range(2000)]
folds = []

for line in lines:
	if 'fold' in line:
		folds.append(line.split()[-1].split('='))
	elif len(line) > 0:
		x, y = line.split(',')
		grid[int(x)][int(y)] = '#'

cnt = 0
for i in range(655):
	for a in range(2000):
		if grid[i][a] == '#' or grid[2 * 655 - i][a] == '#':
			cnt += 1

print(cnt)