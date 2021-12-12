with open('input.txt') as f:
	lines = f.read().splitlines()

lines = [[int(c) for c in line] for line in lines]
cnt = 0

for step in range(100):
	for i in range(10):
		for a in range(10):
			lines[i][a] += 1

	change = True
	flashed = [[False] * 10 for _ in range(10)]
	
	while change:
		change = False
		for i in range(10):
			for a in range(10):
				if lines[i][a] > 9 and not flashed[i][a]:
					flashed[i][a] = True
					change = True
					for k in range(-1, 2):
						for j in range(-1, 2):
							newi = i + k
							newa = a + j
							if 0 <= newi and newi < 10 and 0 <= newa and newa < 10:
								lines[newi][newa] += 1
		
	for i in range(10):
		for a in range(10):
			if flashed[i][a]:
				cnt += 1
				lines[i][a] = 0

print(cnt)