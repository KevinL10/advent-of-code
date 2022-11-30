# Day 20 Solution

### Part 1

Though the image is theoretically infinite in size, we only need to consider the pixels close to the image. In my case, I did the image enhancement on a 600x600 grid, decreasing the number of rows and columns each time (to avoid worrying about the pixels on the edge). Afterward, all we have to do is count the number of `#`s on the remaining grid.

### Part 2

Since 50 is relatively small, we don't have to change anything else.

**Note**: running with [PyPy](https://www.pypy.org/) reduces the runtime from 30 seconds to 5 seconds.

### Thoughts
Forgot that `arr1 = arr2` would pass by reference, but otherwise the problem was pretty straightforward. Currently 103rd, hoping to break through in the next few days...