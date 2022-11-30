with open('input.txt') as f:
	lines = f.read().splitlines()

s = 0

for line in lines:
	uniq, out = line.split(' | ')
	uniq = uniq.split()
	out = out.split()
	
	for c in out:
		if len(c) == 7 or len(c) == 4 or len(c) == 2 or len(c) == 3:
			s += 1

print(s)