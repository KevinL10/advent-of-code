with open('input.txt') as f:
	lines = f.read().splitlines()

# produces True if the board wins
def is_marked(board):
	for i in range(5):
		flag = True
		for a in range(5):
			if board[i][a] != -1:
				flag = False
		if flag:
			return True

	for a in range(5):
		flag = True
		for i in range(5):
			if board[i][a] != -1:
				flag = False
		if flag:
			return True

	return False

def update(board, val):
	for i in range(5):
		for a in range(5):
			if board[i][a] == val:
				board[i][a] = -1
	return board

def sum_board(board):
	s = 0
	for i in range(5):
		for a in range(5):
			if board[i][a] != -1:
				s += int(board[i][a])
	return s

numbers = lines[0].split(',')
boards = []

for i in range(2, len(lines), 6):
	boards.append([line.split() for line in lines[i:i+5]])

finished = [False] * len(boards)

for num in numbers:
	for i in range(len(boards)):
		boards[i] = update(boards[i], num)
		if is_marked(boards[i]) and not finished[i]:
			finished[i] = True
			final = sum_board(boards[i]) * int(num)

print(final)
