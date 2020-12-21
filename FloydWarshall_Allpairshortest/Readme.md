Floyd Warshall Algorithm
===

Find all pairs shortest distance in a graph
[GeeksforGeeks](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)

The DP idea:

* dp[k-1][i][j] stores the shortest distance between all pairs with only first k-1 nodes
* When the k-th node enters, we have the reduction rule
  * dp[k][i][j] = min(dp[k-1][i][j], dp[k-1][i][k] + dp[k-1][k][j])
  * because the k-th node serves as an intermedia nodes along the path
* The space complexity can be reduced to `O(N^2)` by removing the first `k` dimension

Time Complexity: O(V^3)

```
    dist = [[float('inf')] * V for _ in range(V)]
    dist[i][j] = edge_weight[i][j]
    
    for k in range(V): 
        for i, j in itertools.product(range(V), range(V)): 
            dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j]) 
```


LC1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
---
Basically the solution is the code snippet above.
