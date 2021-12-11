with open('input.txt') as f:
	lines = f.read().splitlines()

chars = '([{<'
opp = {'(':')', '[':']', '<':'>', '{':'}'}
scores = []

for line in lines:
	stack = []
	incomplete = True

	for c in line:
		if c in chars:
			stack.append(c)
		elif opp[stack[-1]] != c:
			incomplete = False
			break
		else:
			stack = stack[:-1]

	if incomplete:
		cur = 0
		for c in stack[::-1]:
			cur = cur * 5 + chars.find(c) + 1
		scores.append(cur)

scores.sort()
print(scores[len(scores)//2])