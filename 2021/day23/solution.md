# Day 23 Solution

### Part 1

I solved this part manually, trying to minimize the amount that `D` moved, then `C`, and so on. However, the brute-force solution for Part 2 also works here.

### Part 2

The room structure is quite small, and so we can brute force all possible movements and find the minimum energy to reach the final state. I used Dijkstra's algorithm alongside a priority queue (`heapq`) to keep track of the minimum energy required to reach each state (values in the top row and rooms). 

To find the next possible state, there are two cases: either a value moves out of a room to the top row, or a value from the top row moves into its designated room. In each of the cases, there are a few checks that need to be performed (making sure there aren't any values blocking the path, etc).

### Thoughts
A cool problem, though it seems like quite a few people manually solved Part 2 as well and made it to the leaderboard. 20 points off with 2 days left...