with open('input.txt') as f:
	lines = f.read().splitlines()

chars = '([<{'

s = 0
for line in lines:
	stack = []
	for c in line:
		if c in chars:
			stack.append(c)
		else:
			if c == ')' and stack[-1] != '(':
				s += 3
			elif c == ']' and stack[-1] != '[':
				s += 57
			elif c == '}' and stack[-1] != '{':
				s += 1197
			elif c == '>' and stack[-1] != '<':
				s += 25137
			else:
				stack = stack[:-1]
				continue
			break

print(s)