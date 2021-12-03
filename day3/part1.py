with open('input.txt') as f:
	lines = f.read().splitlines()

most = ''
least = ''

for i in range(len(lines[0])):
	cnt1 = 0
	cnt0 = 0
	for line in lines:
		if line[i] == '0':
			cnt0 += 1
		else:
			cnt1 += 1

	if cnt1 > cnt0:
		most += '1'
		least += '0'
	else:
		most += '0'
		least += '1'

print(int(most, 2) * int(least, 2))