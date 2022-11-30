# Day 8 Solution

### Part 1

Since the digits `1`, `4`, `7`, and `8` are the only digits that use `2`, `4`, `3`, and `7` segments respectively, we can simply count the number of output values with these lengths.

### Part 2

A naive brute-force works by trying out every possible mapping (e.g. from `abcdefg` to `ebfadgc`), and seeing if the ten unique signal patterns match up with the expected segments. In Python, it took around ~5 seconds to go through all the lines in the input.

Alternatively, you can first determine the segments for `1`, `4`, `7`, and `8`, before figuring out the rest of the digits from the segments they have in common.

### Thoughts
A long problem to read through, although there were lots of nice potential solutions to Part 2.