# Day 4 Solution

### Part 1

For each number called, update every board and check whether the board wins. One way to do this is to mark each called number with `-1` and check the rows and columns for five `-1`'s in a row. Alternatively, you can dynamically keep track of how many called numbers are in each row and column of a board.

### Part 2

In addition to updating the boards, use a separate `visited` list to remember which boards have already won. The answer would then be the score of the last board.

### Thoughts
Got caught up with parsing the input, although implementing the solution was pretty straightforward.