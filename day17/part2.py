# Search space
ss = 500

# Make sure to set the bounds to a reasonable number...
def in_bounds(x, y):
	return -ss <= x and x <= ss and -ss <= y and y <= 10000

def in_target(x, y):
	return target_x[0] <= x and x <= target_x[1] and target_y[0] <= y and y <= target_y[1]

target_x = [201, 230]
target_y = [-99, -65]
cnt = 0

for x in range(0, ss):
	for y in range(-ss, ss):
		cur_x = 0
		cur_y = 0
		vx = x
		vy = y

		while in_bounds(cur_x, cur_y):
			cur_x += vx
			cur_y += vy

			vy -= 1
			if vx > 0:
				vx -= 1
			elif vx < 0:
				vx += 1

			if in_target(cur_x, cur_y):
				cnt += 1
				break

print(cnt)