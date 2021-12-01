with open('input.txt', 'r') as f:
	lines = f.readlines()

cnt = 0

for i in range(len(lines) - 1):
	if int(lines[i + 1]) > int(lines[i]):
		cnt += 1

print(cnt)