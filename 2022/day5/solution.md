# Day 5 Solution

### Part 1

After parsing the input, we can simulate the instructions by keeping a list of crate stacks and rearranging the tops of the stacks with some Python list slicing.

### Part 2

The same as part 1, the only change is from `crates[y] = tomove[::-1] + crates[y]` to `crates[y] = tomove + crates[y]`.


### Thoughts

The fastest way to "parse" the input for me was to just manually type it out, though I narrowly missed the leaderboard for part 1. 