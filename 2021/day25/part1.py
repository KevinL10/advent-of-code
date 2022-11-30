import functools
from copy import copy, deepcopy

with open('input2.txt') as f:
	lines = f.read().splitlines()

lines = [list(l) for l in lines]
rows = len(lines)
cols = len(lines[0])

for step in range(1000):
	change = False
	t_lines = deepcopy(lines)
	for i in range(rows):
		for a in range(cols):
			if lines[i][a] == '>' and lines[i][(a + 1) % cols] == '.':
				t_lines[i][(a + 1) % cols] = '>'
				t_lines[i][a] = '.'
				change = True
	lines = deepcopy(t_lines)
	
	for i in range(rows):
		for a in range(cols):
			if lines[i][a] == 'v' and lines[(i + 1) % rows][a] == '.':
				t_lines[(i + 1) % rows][a] = 'v'
				t_lines[i][a] = '.'
				change = True

	lines = deepcopy(t_lines)
	if not change:
		print(step)
		break
