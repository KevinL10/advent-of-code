# Day 12 Solution

### Part 1

We can simulate the rocks and the sand flow using a 2d-array that's large enough to contain all of the rocks and sand (I chose a 1000 x 1000 grid). Then, for each consecutive pair in a path, we label all the indices along that path as a rock on our grid.

To simulate the sand flow, we start at (500, 0) and update the x and y positions depending on our current surroundings. Repeat this until a sand goes beyond the deepest rock (at which point the sand will flow forever).

### Part 2

Similar to Part 1: we now add a line of rocks at 2 rows beyond the maximum depth. Repeatedly simulate the sand flow until the value at (500, 0) becomes a sand particle.

### Thoughts

A short simulation problem where implementing the problem word-for-word is enough. Another option is to use a set to keep track of all of the rocks and sand on the grid.