# Day 7 Solution

### Part 1

As we go through each command, keep track of the current directory that we're in. There are two cases:
- If the current command is `cd`, then we update our current directory
- If the current line contains a number (filesize), then we add that filesize to our current directory and all parent directories.

At the end, we sum up all of the directory sizes less than 100000.

Note: this solution assumes that `ls` is run on each directory at most once.

### Part 2

At the end, we go through the sorted directory sizes until we come across a directory that produces an overall filesystem size of less than 40000000. Since our values are sorted, the first directory that satisfies this will also be the smallest directory.


### Thoughts
A ramp up in difficulty from the past few days! My original solution constructed a directed graph based on the ls commands, and ran a topological sort to first update the leaf directories, then the parents of those, etc.

