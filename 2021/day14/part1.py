with open('input.txt') as f:
	lines = f.read().splitlines()

poly = lines[0]
mp = {}

for line in lines[2:]:
	cur = line.split(' -> ')
	mp[cur[0]] = cur[1]

for i in range(10):
	new_poly = poly[0]
	for a in range(len(poly) - 1):
		new_poly += mp[poly[a:a+2]] + poly[a+1]
	poly = new_poly
	print(poly)

cnts = [poly.count(c) for c in poly]
print(max(cnts) - min(cnts))