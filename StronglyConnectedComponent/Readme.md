Three Algorithms for detection of SCC
===

To check if every node has both paths to and from every other node:

1. DFS/BFS from all nodes:
---
Tarjan's algorithm supposes every node has a depth `d[i]`. Initially, the root has the smallest depth. And we do post-order DFS updates: `d[i] = min(d[j])` for any neighbor `j` of `i`.

    function dfs(i)
        d[i] = i
        mark i as visited
        for each neighbor j of i: 
            if j not visited then dfs(j)
            d[i] = min(d[i], d[j])

If we call `dfs(i)` by the sequence `i = 1,2,..N`, any reachable node from the root have a depth no less than the root. After the post-order DFS updates, since the DFS starting from any nodes can also reach the root, `d[root] <= d[i]` for any reachable node `i` from `root`. All the nodes with the depth of `d[root]` form a SCC.


2. Two DFS/BFS from the single node:
---
Kosaraju’s algorithm 

