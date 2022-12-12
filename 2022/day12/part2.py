with open("input.txt", "r") as f:
    data = f.read()

visited = [[False] * 1000 for i in range(1000)]

arr = [list(s) for s in data.split("\n")]
r = len(arr)
c = len(arr[0])

queue = []
for i in range(r):
    for a in range(c):
        if arr[i][a] == "S" or arr[i][a] == "a":
            queue.append((i, a, 0))
            visited[i][a] = True
            arr[i][a] = "a"
        elif arr[i][a] == "E":
            end = (i, a)
            arr[i][a] = "z"


while queue:
    head = queue.pop(0)
    x, y, s = head

    if (x, y) == end:
        print("Found:", s)
        exit()

    for (dx, dy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        newx = x + dx
        newy = y + dy

        if 0 <= newx and newx < r and 0 <= newy and newy < c:
            if not visited[newx][newy] and ord(arr[newx][newy]) <= ord(arr[x][y]) + 1:
                queue.append((newx, newy, s + 1))
                visited[newx][newy] = True