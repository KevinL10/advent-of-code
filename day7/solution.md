# Day 7 Solution

### Part 1

We can brute force the possible positions that the crabs move to, while keeping track of the minimum fuel cost.

Alternatively, the optimal position is simply the median of the crab positions! See this [Wikipedia article](https://en.wikipedia.org/wiki/Geometric_median) for some cool properties of the geometric median.

### Part 2

Same as Part 1, but the fuel cost from `a` to `b` would be `abs(b - a) * (abs(b - a) + 1) / 2` instead of `abs(b - a)`

### Thoughts
Neat solution using the idea of a geometric median for Part 1, although a straightforward brute force makes this problem quite easy.