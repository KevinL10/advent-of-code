# Day 10 Solution

### Part 1

Using a stack, keep track of all the current open symbols as you go through the string. If you come across a close symbol, it should match up with the current open one at the top of the stack – if not, the string is corrupted and you can add the corresponding points to the final output.

### Part 2

Filter out the corrupted strings using Part 1. By definition, the stack should contain all the open symbols that haven't been closed yet. **Note:** make sure to traverse the stack in the right order (close the most recent symbols first).

### Thoughts
Another standard problem using the idea of a stack (FILO), although unfortunately I missed the leaderboard :(