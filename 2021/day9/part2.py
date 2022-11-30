with open('input.txt') as f:
	lines = f.read().splitlines()

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
visited = [[False] * 1000 for _ in range(1000)]
cnt = 0

def recur(cur_x, cur_y):
	global cnt
	for k in dirs:
		new_x = cur_x + k[0]
		new_y = cur_y + k[1]
		if 0 <= new_x and new_x < len(lines) and 0 <= new_y and new_y < len(lines[0]):
			if int(lines[new_x][new_y]) != 9 and not visited[new_x][new_y]:
				visited[new_x][new_y] = True
				cnt += 1
				recur(new_x, new_y)

sizes = []
for i in range(len(lines)):
	for a in range(len(lines[0])):
		if not visited[i][a] and int(lines[i][a]) != 9:
			recur(i, a)
			sizes.append(cnt)
			cnt = 0

sizes.sort()

print(sizes[-1] * sizes[-2] * sizes[-3])