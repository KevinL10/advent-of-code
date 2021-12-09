from itertools import permutations
import collections

with open('input.txt') as f:
	lines = f.read().splitlines()

c = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
alpha = 'abcdefg'
ans = 0

for line in lines:
	uniq, out = line.split(' | ')
	uniq = uniq.split()
	out = out.split()

	# Brute force all possible mappings of 'abcdefg' => '......'
	for mapping in permutations('abcdefg'):
		correct = True
		for val in uniq:
			new_val = ''.join([mapping[alpha.find(c)] for c in val])

			# Check that these new segments are an actual number
			if not any([sorted(list(new_val)) == sorted(list(c[k])) for k in range(10)]):
				correct = False
				break

		if correct:
			break

	num = ''
	for val in out:
		new_val = ''.join([mapping[alpha.find(c)] for c in val])
		for k in range(10):
			if sorted(list(new_val)) == sorted(list(c[k])):
				num += str(k)
				
	ans += int(num)

print(ans)