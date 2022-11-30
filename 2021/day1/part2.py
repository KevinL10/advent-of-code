with open('input.txt', 'r') as f:
	lines = f.readlines()

cnt = 0

for i in range(len(lines) - 3):
	if int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3]) > int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2]):
		cnt += 1

print(cnt)