with open('input.txt') as f:
	lines = f.read().splitlines()

row = len(lines)
col = len(lines[0])

dp = [[10 ** 100] * 1000 for _ in range(1000)]
dp[0][0] = 0

for i in range(row):
	for a in range(col):
		if i == 0 and a == 0:
			continue
		if a - 1 >= 0:
			dp[i][a] = min(dp[i][a], dp[i][a-1])
		if i - 1 >= 0:
			dp[i][a] = min(dp[i][a], dp[i - 1][a])
		dp[i][a] += int(lines[i][a])

print(dp[row - 1][col - 1])