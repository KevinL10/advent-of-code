# Day 21 Solution

### Part 1

An easy way to solve this is to repeatedly loop through the list of monkeys and update each monkey if it's a number or its predecessors have already yelled. Everytime a monkey yells their value, we set the `changed` variable to `True` to signify that there was an update. If the `changed` variable is `False` after looping through all the monkeys, then no further updates are possible and we stop the loop.

An alternative solution is to consider the monkeys as a directed graph, where the monkeys with numbers are leaves and the rest of the monkeys point to the monkeys that they depend upon. Then, you can run a topological sort to produce an order for traversing the graph once. 

### Part 2

An observation is that changing the value of your monkey, `humn`, is directly correlated with the `root` monkey in a way that makes binary search possible. Specifically, increasing the value of `humn` will decrease the value of `root`, and decreasing `humn` will increase `root`. Note: depending on your puzzle input this may be the other way around.

Using this observation, we can perform a simple binary search and repeatedly loop our part 1 code with the `humn` variable initialized to our current binary search value. Once we find a value that satisfies `root's` equality, we're finished.

You can also use a symbolic solver such as `z3`. You have one unknown variable (`humn`) and you want to satisfy equality between `root's` numbers.

### Thoughts

Fun problem with lots of alternative solutions. It turns out that using floating-point division (`/`) and integer division (`//`) in Python produced slightly different answers on some problem inputs -- be careful!