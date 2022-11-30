# Day 21 Solution

### Part 1

We can simulate the game, keeping track of the players' positions and scores, as well as the value of the die. A nice way of making sure `x` wraps back to 1 from 10 is by writing `(x + steps - 1) % 10 + 1`.

### Part 2

Since each game splits into multiple copies, we can use a recursive function to find the total number of ways each player wins given a current state (whose turn, positions, scores). A naive brute force would run in `O(3^n)` (which would be too slow); we can speed things up by using memoization to store the results of intermediate states.

### Thoughts
Typod `p1` for `p2` in part 2 which cost me ~ 10 minutes and top 20 on the leaderboard :( 