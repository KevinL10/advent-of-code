# Day 17 Solution

### Part 1

Since the distances are relatively small (~100), we can brute force all possible velocities (in the `x` and `y` directions), keeping track of the maximum height for each.

### Part 2

Instead of storing the maximum height, instead update a count for each velocity that lands in the target area.

### Thoughts
A nice break from the more tedious/complicated problems. Luckily I caught a bug in time for the leaderboard (I had stopped the trajectory prematurely before it reached the target). Hoping that I can stay in top 100 for the remaining few days (currently 97th)...