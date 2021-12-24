import functools

with open('input.txt') as f:
	lines = f.read().splitlines()

# split the input into blocks starting with `inp w`
blocks = []
cur_block = []

for line in lines:
	instr = line.split(' ')
	if instr[0] == 'inp':
		assert(instr[1] == 'w')
		blocks.append(cur_block)
		cur_block = []
	else:
		cur_block.append(instr)

blocks.append(cur_block)
blocks = blocks[1:]

chars = 'wxyz'
dp = {}

# return the z value after the block at `idx`, given the current `w` and `z` values
def asm(idx, w, z):
	vals = [w, 0, 0, z]
	# each instr is `op a b`
	for instr in blocks[idx]:
		idx = chars.index(instr[1])
		# store the value of b
		if instr[2].lstrip('-').isdigit():
			val = int(instr[2])
		else:
			val = vals[chars.index(instr[2])]

		if instr[0] == 'add':
			vals[idx] += val
		elif instr[0] == 'mul':
			vals[idx] *= val
		elif instr[0] == 'div':
			vals[idx] = int(vals[idx]/val)
		elif instr[0] == 'mod':
			vals[idx] = vals[idx] % val
		else:
			assert(instr[0] == 'eql')
			vals[idx] = int(vals[idx] == val)

	return vals[3]

path = []

# return True if it's possible to reach the end, given the current `z` value and block we're at
@functools.cache
def recur(idx, cur_z):
	global path
	if idx == len(blocks):
		if cur_z == 0:
			print(''.join([str(p) for p in path]))
			return True
		return False

	# try all w from 9 => 1 since we want to maximize w
	for w in range(9, 0, -1):
		path.append(w)
		if recur(idx + 1, asm(idx, w, cur_z)):
			return True
		path = path[:-1]
	return False

recur(0, 0)