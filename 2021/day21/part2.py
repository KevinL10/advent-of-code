with open('input.txt') as f:
	lines = f.read().splitlines()

mp = {}

def recur(turn, p1, p2, s1, s2):
	key = str(turn) + ' ' + str(p1) + ' ' + str(p2) + ' ' + str(s1) + ' ' + str(s2)

	if key in mp:
		return mp[key]

	if s1 >= 21:
		return [1, 0]
	if s2 >= 21:
		return [0, 1]

	ans = [0, 0]

	if turn == 1:
		for i in range(1, 4):
			for j in range(1, 4):
				for k in range(1, 4):
					new_p1 = (p1 + i + j + k - 1) % 10 + 1
					res = recur(2, new_p1, p2, s1 + new_p1, s2)
					ans[0] += res[0]
					ans[1] += res[1]
			
	else:
		for i in range(1, 4):
			for j in range(1, 4):
				for k in range(1, 4):
					new_p2 = (p2 + i + j + k - 1) % 10 + 1
					res = recur(1, p1, new_p2, s1, s2 + new_p2)
					ans[0] += res[0]
					ans[1] += res[1]
	mp[key] = ans
	return ans

print(max(recur(1, 10, 7, 0, 0)))