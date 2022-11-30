with open('input.txt') as f:
	lines = f.read().splitlines()

states = lines[0].split(',')
states = [int(k) for k in states]

cnt = [0] * 9

for s in states:
	cnt[s] += 1

for i in range(256):
	new_fish = cnt[0]

	for a in range(0, 8):
		cnt[a] = cnt[a + 1]

	cnt[8] = new_fish
	cnt[6] += new_fish

print(sum(cnt))
