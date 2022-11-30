with open('input.txt') as f:
	lines = f.read().splitlines()

def recur(cur, path, twice):
	if cur == 'end':
		return 1

	out = 0
	for child in adj[cur]:
		if child == 'start':
			continue
		elif child.lower() != child or child not in path:
			out += recur(child, path + [child], twice)
		elif path.count(child) == 1 and not twice:
			out += recur(child, path + [child], True)
	return out

adj = {}

for line in lines:
	v1, v2 = line.split('-')
	adj.setdefault(v1,[]).append(v2)
	adj.setdefault(v2,[]).append(v1)

print(recur('start', ['start'], False))