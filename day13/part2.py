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
		
for f in folds:
	val = int(f[1])
	if f[0] == 'x':
		for i in range(val):
			for a in range(2000):
				if grid[i][a] == '#' or grid[2 * val - i][a] == '#':
					grid[i][a] = '#'
	else:
		for i in range(2000):
			for a in range(val):
				if grid[i][a] == '#' or grid[i][2 * val - a] == '#':
					grid[i][a] = '#'	

for i in range(40):
	print(''.join(grid[i][:6][::-1]))

#JRZBLGKH