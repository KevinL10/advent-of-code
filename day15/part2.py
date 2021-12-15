from heapq import heappop, heappush

with open('input.txt') as f:
    lines = f.read().splitlines()

row = len(lines)
col = len(lines[0])
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# returns integer at position (x, y)
def val(x, y):
    num = int(lines[x % row][y % col]) + x // row + y // col
    return (num - 1) % 9 + 1

def in_bounds(x, y):
    return 0 <= x and x < 5 * row and 0 <= y and y < 5 * col

dist = [[10 ** 100] * 5 * row for i in range(5 * col)]
# (dist, x, y)
queue = [(0, 0, 0)]
dist[0][0] = 0

while len(queue) != 0:
    d, x, y = heappop(queue)
    if x == 5 * row - 1 and y == 5 * col - 1:
        print(d)

    for k in dirs:
        new_x = x + k[0]
        new_y = y + k[1]
        if in_bounds(new_x, new_y) and dist[x][y] + val(new_x, new_y) < dist[new_x][new_y]:
            dist[new_x][new_y] = dist[x][y] + val(new_x, new_y)
            heappush(queue, (dist[new_x][new_y], new_x, new_y))