with open('input.txt') as f:
	lines = f.read().splitlines()

p1 = 10
p2 = 7
s1 = 0 
s2 = 0

dice = 1
turn = 1

while True:
	if s1 >= 1000 or s2 >= 1000:
		# min(s1, s2) is the score below 1000, while dice - 1 is the number of total rolls
		print(min(s1, s2) * (dice - 1))
		break

	rolls = 0
	for i in range(3):
		rolls += (dice + i - 1) % 100 + 1

	if turn == 1:
		p1 = (p1 + rolls - 1) % 10 + 1
		s1 += p1
	else:
		p2 = (p2 + rolls - 1) % 10 + 1
		s2 += p2

	# Flip whose turn it is and increase the dice value
	turn = 3 - turn
	dice += 3
