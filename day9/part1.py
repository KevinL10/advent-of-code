with open('input.txt') as f:
	lines = f.read().splitlines()

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
s = 0

for i in range(len(lines)):
	for a in range(len(lines[0])):
		for k in dirs:
			new_i = i + k[0]
			new_a = a + k[1]
			if 0 <= new_i and new_i < len(lines) and 0 <= new_a and new_a < len(lines[0]) and int(lines[i][a]) >= int(lines[new_i][new_a]):
				break
		else:
			s += (int(lines[i][a]) + 1)

print(s)