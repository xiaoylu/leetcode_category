Max Flow
---

Problem:

* Input: a graph with edge capacity, source `s` and destination `t`
* Output: max flow from s to t  (the flow over every edge is no more than its capacity)

Maximum flow can be used for max matching in bi-parite graph if we create a fake source S and fake destination T, 
each connecting to the nodes of one layer in the bi-parite graph.

Edmonds-Karp implementation of the Ford-Fulkerson algorithm:

* repeat forever
  * Create a residual graph `rG`, for an edge `u -> v` in original graph `G`
    * rG[u][v] = G[u][v]
    * rG[v][u] = 0

  * BFS to find a shortest path from s to t with postive flow
  
  * If no such path: break
  
  * For each edge in this path:
    * Remove the bottleneck flow in the forward edges
    * Add the bottleneck flow in the reverse edges

```

```
