Sparse Table
===

Given a list of numbers, you do not need to update them. How much time you need to query min element in a range?

It is only `O(1)` time using sparse table!

[Sparse Table (GeekforGeeks)](https://www.geeksforgeeks.org/sparse-table/)

Using segment tree, it is `O(log n)` time for each query. But you can update the array in `O(log n)` time.

Always ask yourself:

Can we do better if we know that array is static?


See more about [Range Min Query (RMQ)](https://www.geeksforgeeks.org/range-minimum-query-for-static-array/) using Square Root Decomposition.
