# Day 11 Solution

### Part 1

For each step, first increment all of the values in the grid. Afterward, for each octopus with energy level above 9, update its neighbours and repeat until there aren't any possible flashes left. You can keep track of which octopuses have flashed and sum up the count across the 100 steps.

### Part 2

Instead of stopping at 100 steps, continue until you reach 100 flashes in a single step.

### Thoughts
Similar to some of the Game-of-Life-type problems from 2020, though I made quite a few mistakes during the initial implementation.