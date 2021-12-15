with open('input.txt') as f:
	lines = f.read().splitlines()

poly = lines[0]
mp = {}
cnt = {}

for line in lines[2:]:
	cur = line.split(' -> ')
	mp[cur[0]] = cur[1]

for i in range(len(poly) - 1):
	cnt[poly[i:i+2]] = cnt.get(poly[i:i+2], 0) + 1

for i in range(40):
	cnt2 = {}
	for pair in cnt:
		cnt2[pair[0] + mp[pair]] = cnt2.get(pair[0] + mp[pair], 0) + cnt[pair]
		cnt2[mp[pair] + pair[1]] = cnt2.get(mp[pair] + pair[1], 0) + cnt[pair]
	cnt = cnt2

lst = {}
for pair in cnt:
	lst[pair[0]] = lst.get(pair[0], 0) + cnt[pair]
lst[poly[-1]] += 1

print(max(lst.values()) - min(lst.values()))