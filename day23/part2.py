from heapq import heappush, heappop
from copy import copy, deepcopy

cost_map = {'A':1, 'B':10, 'C':100, 'D':1000}
indices = {'A':2, 'B':4, 'C':6, 'D':8}
chars = 'ABCD'

def sign(x):
	if x < 0:
		return -1
	else:
		return 1

# Produce a list of all possible next states given the current state (top row and the rooms)
# (cost, top, rooms)
def next_states(top, rooms):
	out = []
	# Case 1: outmost value in a room moves to the top row
	for i in range(4):
		# If all the values are already in the right place, doesn't remove them
		if all([c == chars[i] or c == '.' for c in rooms[i]]):
			continue

		# Find the index of the outermost value
		for a in range(4):
			if rooms[i][a] != '.':
				break

		t_rooms = deepcopy(rooms)
		t_rooms[i][a] = '.'
		val = rooms[i][a]

		# You can move the value to the left or right of the room's position in the top row
		for direction in [-1, 1]:
			if direction == -1:
				bound = -1
			else:
				bound = 11

			for j in range(indices[chars[i]], bound, direction):
				# If there's another value, then you can't move it any further
				if top[j] != '.':
					break
				if j == 2 or j == 4 or j == 6 or j == 8:
					continue

				# Otherwise, you can move the new value to position j
				t_top = deepcopy(top)
				t_top[j] = val
				cost = (a + 1 + abs(indices[chars[i]] - j)) * cost_map[val]
				out.append((cost, t_top, t_rooms))

	# Case 2: value from the top row moves into a room
	for i in range(11):
		if top[i] == '.':
			continue

		val = top[i]
		idx = chars.index(val)

		# Check that all the chars in your target room are correct
		if not all([c == val or c == '.' for c in rooms[idx]]):
			continue

		# Check that there aren't any other values blocking the path to the room
		s = sign(indices[val] - i)
		if any([top[j] != '.' for j in range(i + s, indices[top[i]] + s, s)]):
			continue

		# Find the index of the outermost value in the room
		for j in range(4):
			if rooms[idx][j] == top[i]:
				break
		else:
			j = 4

		t_top = deepcopy(top)
		t_rooms = deepcopy(rooms)
		# Update top row and rooms
		t_top[i] = '.'
		t_rooms[idx][j - 1] = val

		# Energy is the (horizontal distance + vertical distance) * multiplier
		cost = (abs(indices[val] - i) + j) * cost_map[val]
		out.append((cost, t_top, t_rooms))

	return out

# return True if the state is organized
def is_end(top, rooms):
	for i in range(4):
		if rooms[i] != [chars[i]] * 4:
			return False

	assert(top == ['.'] * 11)
	return True

rooms = [[] for i in range(4)]
rooms[0] = list('CDDB')
rooms[1] = list('DCBA')
rooms[2] = list('DBAB')
rooms[3] = list('AACC')

top = list('...........')
q = [(0, top, rooms)]
visited = set()

while len(q) != 0:
	energy, top, rooms = heappop(q)
	# Avoid recomputing states you've already visited
	key = ''.join(top)
	for i in range(4):
		key += ''.join(rooms[i])
	if key in visited:
		continue
	visited.add(key)

	if is_end(top, rooms):
		print('Found:', energy)
		exit()

	new_states = next_states(top, rooms)
	for cost, t, r in new_states:
		heappush(q, (energy + cost, t, r))
