# Day 8 Solution

### Part 1

For each element in the grid at (r, c), we can tell whether it's visible from a direction by iterating through all of the elements to the edge and checking that they're less than the current value. This involves the (inclusive) ranges:
- Up: from 0 ... r-1
- Down: from r+1 ... rows-1 
- Left: from 0 ... c-1
- Right: from c+1 ... cols-1

If they're visible from any of the directions, then we increment the total count by 1.

### Part 2

Similar to Part 1, but we also keep track of how *far* we can go in each direction with separate variables for each.


### Thoughts
There are more optimal solutions, but this naive method is fast enough for small inputs.
