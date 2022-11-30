with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

x = 0
y = 0
for line in lines:
	instr, val = line.split(' ')
	val = int(val)
	if instr == 'forward':
		x += val
	elif instr == 'down':
		y += val
	elif instr == 'up':
		y -= val

print(x * y)