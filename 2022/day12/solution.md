# Day 12 Solution

### Part 1

We can solve this problem with a standard BFS. Start at the element containing "S"; at each step, we can move to one of the 4 neighbouring cells if the new element is at most 1 character away lexicographically, i.e. `ord(arr[newx][newy]) <= ord(arr[x][y]) + 1`

### Part 2

To account for the other starting points, we can simply add them to the queue before starting the BFS.


### Thoughts

This problem was pretty standard - I didn't have a pre-written BFS template, but the implementation was simple enough to complete in a few minutes.