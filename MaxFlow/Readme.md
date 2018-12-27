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
'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

from collections import defaultdict
from collections import deque

def maxflow(G, s, t, N):
    # Given graph G with N nodes
    # return the max flow from source s to destination t
    rG = collections.defaultdict(dict)
    for u in G:
        for v in G[u]:
            rG[u][v] = G[u][v]
            rG[v][u] = 0
            
    max_flow = 0
    while True:
        # bfs to find shortest path with postive flow
        parent = [-1] * N
        vis = set([s])
        bfs = deque([s])
        while bfs:
            u = bfs.popleft()
            if u == t:
                break
            for v in rG[u]:
                if v not in vis and rG[u][v] > 0:
                    vis.add(v)
                    parent[v] = u
                    
        # terminate when no augment path found
        if parent[t] == -1: break
            
        # find bottleneck
        v = t
        bottleneck = float('inf')
        while v != s:
            u = parent[v]
            bottleneck = min(bottleneck, rG[u][v])
            v = u
            
        # remove bottleneck flow
        v = t
        while v != s:
            u = parent[v]
            rG[u][v] -= bottleneck
            rG[v][u] += bottleneck
            v = u
            
        max_flow += bottleneck
    return max_flow
        
# preference [[0,1,2,3],[0,1,2],[0,1],[1,2]]
# max matching is x0->y3, x1->y1, x2->y0, x3->y2

preference = [[0,1,2,3],[0,1,2],[0,1],[1,2]]
N = len(preference)
G = defaultdict(dict)
s, t = 0, 1
for i in range(N):
    G[s][2 + i] = 1 # source to layer one
    G[2 + N + i][t] = 1 # layer two to destination
for i, row in enumerate(preference):
    for r in row:
        G[2 + i][2 + N + r] = 1 
print(maxflow(G, s, t, N))
```
