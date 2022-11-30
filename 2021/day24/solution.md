# Day 24 Solution

### Part 1

Note that the instructions consist of almost identical sections, each beginning with `inp w`. Afterward, the `x` and `y` registers are reset, and the resulting `z` is calculated. In other words, we can treat each section as a black box that takes in `w` and `z`, returning a new `z`.

A brute force would take `O(9^n)` for `n` sections, so we can instead solve this recursively. At each section, given the current values for `w` and `z`, we determine whether it's possible to reach the target `z = 0` at the end. Since we want to find the maximum model number, we can try all `w` values starting from `9` to `1`, keeping track of the path in a separate stack.

With memoization (`@functools.cache`), the code runs in ~18 seconds.

### Part 2

Unfortunately, naively trying `w` values in the other direction (from `1` to `9`) turns out to be too slow. Instead, we can cut off recursive calls once the `z` value exceeds a certain number, because we're only looking for the *minimum* model number (`w` values). With a bit of trial and error, I found that 10^6 produced a solution in around 6 seconds.

### Thoughts
Another fun problem with a small but interesting twist in part 2. Luckily, I made it back onto the leaderboard (100th place with 1 day left)!