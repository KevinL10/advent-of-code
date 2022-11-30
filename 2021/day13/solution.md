# Day 13 Solution

### Part 1

For every fold in the x-direction along `x'`, the coordinate `(x, y)` will be marked if either `(x, y)` or the point on the other side of the fold, `(2 * x' - x, y)`, were marked. Similarly, for a fold along `y'`, the point `(x, y)` will be marked if at least one of `(x, y)` and `(x, 2 * y' - y)` are marked.

### Part 2

Note that folding a paper along `x=x'` makes the length of the paper (in the x-direction) `x'`. The final folds in each direction are `x=40` and `y=6`, so we only need to print out the first 40 rows with 6 characters each.

### Thoughts
A small typo (`==` instead of `=`) cost me 900 ranks... otherwise, this was a pretty neat problem.