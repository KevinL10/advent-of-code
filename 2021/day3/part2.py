with open('input.txt') as f:
	lines = f.read().splitlines()

most_common = lines
least_common = lines

for i in range(len(most_common[0])):
	cnt0 = 0
	cnt1 = 0

	# find the most common character
	for line in most_common:
		if line[i] == '0':
			cnt0 += 1
		else:
			cnt1 += 1

	if cnt1 >= cnt0:
		c = '1'
	else:
		c = '0'

	# filter out values that don't have the correct character
	most_common = [line for line in most_common if line[i] == c]

	cnt0 = 0
	cnt1 = 0

	# find the least common character
	for line in least_common:
		if line[i] == '0':
			cnt0 += 1
		else:
			cnt1 += 1

	# take care of the case where there's only 1 element left
	if cnt0 == 0:
		c = '1'
	elif cnt1 == 0 or cnt0 <= cnt1:
		c = '0'
	else:
		c = '1'

	# filter out values that don't have the correct character
	least_common = [line for line in least_common if line[i] == c]

print(int(least_common[0], 2) * int(most_common[0], 2))