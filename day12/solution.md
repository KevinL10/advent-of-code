# Day 12 Solution

### Part 1

We can represent the graph using an adjacency list, with `adj[v1]` containing all the edges to/from `v1`. Then, we run a DFS beginning at the `start` node: in my implementation, `recur(cur, path)` returns the number of ways to reach `end` from the current node (`cur`) and having visited the nodes in `path`. Finally, we recurse on every child node that's upper-case or hasn't been visited yet.

### Part 2

In addition to storing the nodes we've alreay visited, we also keep track of whether or not we've visited a small cave twice already. If we haven't, then we can re-visit a node that appears once in our current path.

(Although not necessary), we can also speed things up with dynamic programming — keep track of the output value for each state to avoid recomputation.

### Thoughts
Graph theory problems are pretty fun :)