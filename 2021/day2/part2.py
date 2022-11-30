with open('input.txt', 'r') as f:
	lines = f.read().splitlines()

x = 0
y = 0
aim = 0
for line in lines:
	instr, val = line.split(' ')
	val = int(val)
	if instr == 'forward':
		x += val
		y += aim * val
	elif instr == 'down':
		aim += val
	elif instr == 'up':
		aim -= val

print(x * y)