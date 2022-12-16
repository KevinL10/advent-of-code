# Day 10 Solution

### Part 1

An easy way to implement this is to always increment the cycle count, but only increment it again if the current instruction is an `addx` instruction. We update the total strength after the first increment and after both the second increment and X register update. 

### Part 2

This time, we check whether the current cycle lies on the sprite's position *before* the first increment and *before* the second increment. We only update the X register after both increments have completed, similar to Part 1.

### Thoughts
The core idea for this problem is relatively simple, but it's extremely easy to make off-by-one errors like updating the cycle counter after instead of before drawing the pixel.