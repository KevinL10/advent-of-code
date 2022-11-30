# Day 24 Solution

### Part 1

We first process the sea cucumbers moving east, then use the new grid to process the cucumbers moving south. To deal with the wrap-around, we can write `x % rows` and `y % cols` for `(x, y)`.

### Thoughts
A small and simple problem to wrap everything up for this year! I missed my goal of top 100 by two places ([102nd](https://freedomofkeima.github.io/aoc-ranking/)), but I'm looking forward to trying again next year :)