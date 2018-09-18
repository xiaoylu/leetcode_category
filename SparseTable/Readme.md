Sparse Table
===

> `O(n logn)` time pre-processing and `O(1)` time query.
> `d[i][j]` stores the max/min element in `[ i, i+(1<<j) )` (inclusive-exclusive)
> DP construction time of `d[i][j]` for at most `O(logn)` values of `j`s
> When query, just return the max/min of `d[l][j]` and `d[r-(1<<j)][j]`

Very short implementation in Python
```
    # sparse table
    d = defaultdict(dict)
    for j in range(N):
        for i in range(N):
            if i + (1<<j) > N: break
            d[i][j] = min(d[i][j-1], d[i + (1<<(j-1))][j-1]) if j > 0 else A[i]

    def query(u, d, l, r): # [l, r) inclusive-exclusive
        j = int(math.log(r - l, 2))
        return min(d[l][j], d[r-(1<<j)][j])
```

Relationship to Segment Tree
===
Given a list of numbers, you do not need to update them. How much time you need to query min element in a range?
It is only `O(1)` time using sparse table!

[Sparse Table (GeekforGeeks)](https://www.geeksforgeeks.org/sparse-table/)

Using segment tree, it is `O(log n)` time for each query. But you can update the array in `O(log n)` time.

Always ask yourself:

Can we do better if we know that array is static?


See more about [Range Min Query (RMQ)](https://www.geeksforgeeks.org/range-minimum-query-for-static-array/) using Square Root Decomposition.
