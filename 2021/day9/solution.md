# Day 9 Solution

### Part 1

Traverse the 2d array, comparing each value with its neighbors (left, right, up, down). A clean way of coding this is using an array `dir` that stores the possible directions.

### Part 2

This problem is fairly standard, commonly known as [Flood Fill](https://en.wikipedia.org/wiki/Flood_fill). We keep track of which nodes (positions in the 2d array) we've already visited, and run a [DFS](https://en.wikipedia.org/wiki/Depth-first_search) for each. You can easily count the number of positions each search visits through some global variable `cnt`.

### Thoughts
First problem where recursion was necessary, looking forward to the other ones!