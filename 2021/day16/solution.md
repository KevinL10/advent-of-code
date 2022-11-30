# Day 15 Solution

### Part 1

One way to solve this recursively is by going through each subpacket at a time: if `packet` represents something like `packet1||packet2||packet3`, then `recur(packet)` parses `packet1` while returning `packet2||packet3` and the total version of `packet1` (including its subpackets). When the type id is `4`, we can directly return the remaining packets and the current version; otherwise, we have to add up all the versions of the subpackets instead.

### Part 2

Similar to Part 1, except we return the value of the current packet instead of the total version. In the case when type id is `4` this is still pretty straightforward; otherwise, we recursively find all the values of the subpackets and perform the associated operation.

### Thoughts
A cool problem with a not-so-trivial recursive step