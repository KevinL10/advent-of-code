# Day 15 Solution

### Part 1

The problem of finding the shortest path is fairly standard; we can either approach it recursively or with dynamic programming. In my case, `dp[i][a]` stores the minimum risk needed to reach `(i, a)`. Since the submarine can only come from `(i - 1, a)` or `(i, a - 1)`, we can take the minimum of those values and add the current risk to get `dp[i][a]`. In other words, the recurrence relation is: `dp[i][a] = min(dp[i-1][a], dp[i][a-1]) + val[i][a]`.

### Part 2

First, note that the value at `(x, y)` is given by `val[x % row][y % col]) + x // row + y // col`, where `x // row` and `y // col` are the number of times the board is shifted in each direction. To include the value wrapping back around, we can add `(val[x][y] - 1) % 9 + 1`.

In this part, the down-right path apparently isn't the most optimal — instead, we need to take into account movement in all four directions. We can directly use a shortest path algorithm like [Dijkstra's](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), maintaining the states `(dist_so_far, x_pos, y_pos)` in a priority queue (`heapq` in Python).

### Thoughts
I spent a while stuck on Part 2 since I thought the only valid moves were downward and to the right. Otherwise, this was a pretty fun graph theory problem.