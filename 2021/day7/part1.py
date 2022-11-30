with open('input.txt') as f:
	lines = f.read().splitlines()

crabs = lines[0].split(',')
crabs = [int(k) for k in crabs]

curmin = 10 ** 100

for i in range(2000):
	cost = sum([abs(c - i) for c in crabs])
	curmin = min(curmin, cost)

print(curmin)