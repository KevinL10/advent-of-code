# Day 14 Solution

### Part 1

We can naively simulate the insertion for each pair, adding the left character and the new character. For example, the rules `NN -> C, NC -> B` for `NNC` would give `NC + NB (+ C) = NCNBC`.

### Part 2

Instead of storing the entire string, you can instead count the number of times each pair occurs. Following the above example, the next step for `NNC` would increase the count for the pairs `NC, CN, NB, BC`. Afterward, we can sum the leftmost character of each pair and the rightmost character of the initial string to get the total times each letter occurs.

### Thoughts
Similar idea to Day 6, where we optimized the code for part 2 by storing a different state.