# Day 4 Solution

### Part 1

Either the first range contains the second, or the second range contains the first. The first case looks something like:

```
----x0------y0-----
--x1-----------y1--
```

So, we can check that `x1 <= x0` and `y0 <= y1`. The other case is similar, just with the variables flipped around.


### Part 2

An easy way to check for overlap is by comparing the larger start position and the smaller ending position. 

If `max(x0, x1) <= min(y0, y1)`, then we have overlap:

```
----x0-------y0------
--------x1-------y1--
```


### Thoughts

Nothing too complicated today, the overlap check for part 2 is a nice-to-know trick.