# Day 6 Solution

### Part 1

A naive implementation would be to simulate the exact process; for each fish with timer `0`, reset its timer to `6` and add another fish with timer `8` to the list.

### Part 2

Since we only care about the *number* of fishes with each timer value, the current state can be represented by a list of length `9`.

### Thoughts
The problem's wording was a bit confusing, although the solution was relatively simple.