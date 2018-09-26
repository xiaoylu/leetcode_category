# Strongly Connected Component (SCC)


## To check if every node has both paths to and from every other node in a given graph:

DFS/BFS from all nodes:
---
[Tarjan's algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm) supposes every node has a depth `d[i]`. Initially, the root has the smallest depth. And we do the post-order DFS updates `d[i] = min(d[j])` for any neighbor `j` of `i`. Actually BFS also works fine with the reduction rule `d[i] = min(d[j])` here.

    function dfs(i)
        d[i] = i
        mark i as visited
        for each neighbor j of i: 
            if j is not visited then dfs(j)
            d[i] = min(d[i], d[j])

If there is a forwarding path from `u` to `v`, then `d[u] <= d[v]`. In the SCC, `d[v] <= d[u] <= d[v]`, thus, all the nodes in SCC will have the same depth. To tell if a graph is a SCC, we check whether all nodes have the same `d[i]`.

Two DFS/BFS from the single node:
---
It is a simplified version of the [Kosaraju’s algorithm](https://www.geeksforgeeks.org/strongly-connected-components/). Starting from the root, we check if every node can be reached by DFS/BFS. Then, reverse the direction of every edge. We check if every node can be reached from the same root again. See [C++ code](http://codeforces.com/contest/475/submission/8140615).

## Find SCC

The most useful and fast-coding algorithm for finding SCCs is Kosaraju.

1. DFS on the graph and sort the vertices in decreasing of their finishing time (we can use a stack `L`).
2. Reverse the graph edges
2. Start from the vertex with the greatest finishing time, and for each vertex v that is not yet in any SCC, do : 
3. for each u that v is reachable by u and u is not yet in any SCC, put it in the SCC of vertex v.

Suppose the nodes are arranged in `L` in post-order after the first round of DFS. `u->v` indicates that there exists a forwarding path from `u` to `v`.

If `u->v` and not `v->u`, then `u` must appear at the left of `v` in `L`. The nodes in a SCC, such as `v` and `w`, however, may appear in arbitrary order in `L`.

![Illustration](https://github.com/xiaoylu/leetcode_category/blob/master/StronglyConnectedComponent/Kosaraju.png)

Among the nodes which can reach `v`, we need to eliminate those `v` can NOT reach. We just skip the nodes on the left of `v` in `L`. That is why we use the nodes in `L` from left to right iteratively as root of the second round DFS.



