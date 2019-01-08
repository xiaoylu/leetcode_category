# Strongly Connected Component (SCC)


## To check if every node has both paths to and from every other node in a given graph:

DFS/BFS from all nodes:
---
[Tarjan's algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm) supposes every node has a depth `d[i]`. Initially, the root has the smallest depth. And we do the post-order DFS updates `d[i] = min(d[j])` for any neighbor `j` of `i`. Actually BFS also works fine with the reduction rule `d[i] = min(d[j])` here.

```
def tarjan(graph):
    d = {i:i for i in range(N)}
    vis = set()
    stack = set()
    def dfs(i):
        vis.add(i)
        stack.add(i)
        for j in graph[i]:
            if j not in vis:
                dfs(j)
                d[i] = min(d[i], d[j])
            elif j in stack:
                d[i] = min(d[i], d[j])
        stack.remove(i)
    for i in range(N):
        if i not in vis:
            dfs(i)
```

If there is a forwarding path from `u` to `v`, then `d[u] <= d[v]`. In the SCC, `d[v] <= d[u] <= d[v]`, thus, all the nodes in SCC will have the same depth. To tell if a graph is a SCC, we check whether all nodes have the same `d[i]`.

Two DFS/BFS from the single node:
---
It is a simplified version of the [Kosaraju’s algorithm](https://www.geeksforgeeks.org/strongly-connected-components/). Starting from the root, we check if every node can be reached by DFS/BFS. Then, reverse the direction of every edge. We check if every node can be reached from the same root again. See [C++ code](http://codeforces.com/contest/475/submission/8140615).

## Find SCC

The most useful and fast-coding algorithm for finding SCCs is Kosaraju.

1. The first DFS pushes every node to a stack in post-order
2. Reverse the graph edges!!
3. Keep poping up source node from stack, the second DFS adds all reachable nodes to the SCC of the source node

Why it works? Say `u` is at the top of stack, if there exists a path from `v -> u`, then `u -> v`.

Proof by contradiction: otherwise, `v` should be above `u` in the stack, then `u` should not be at the top.

Implementation trick:

The first and second DFS can share the same `visited` array. The dfs1 starts with all-false `visited` and set the visited nodes as `true`. And dfs2 starts with the all-true `visited` and set the visited nodes as `false`.

```
        N = len(graph)
        stack = []
        vis = set()
        SCC = {}
        
        rgraph = [[] for _ in range(N)]
        for i in range(N):
            for j in graph[i]:
                rgraph[j].append(i)
        
        def dfs1(i):
            if i not in vis:
                vis.add(i)
                for j in graph[i]:
                    dfs1(j)
                stack.append(i)
                
        for i in range(N): dfs1(i)
        
        def dfs2(i, scc):
            if i in vis:
                vis.remove(i)
                SCC[i] = scc
                for j in rG[i]:
                    dfs2(j, scc)
     
        while stack:
            i = stack.pop()
            dfs2(i, i)
        
        print(SCC)
```
