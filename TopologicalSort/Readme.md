# Topological Sort
To find out the order of nodes in a [DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph)
* remove the node with out-degree ZERO iteratively
* update the degree of other node pointing to this removed node

Keep doing this you will obtain a topological order of the nodes

The application of topological sort:
* Find cycles in a graph. The steps above will remove every node until only some loop of nodes remain.
* Rank prerequisites to find a total order.
* Find the "most inner" nodes in graph, like **LC 310. Minimum Height Trees**.

**LC 310. Minimum Height Trees**
Find the leaves of the tree, and remove the deg 1 nodes iteratively until no more than two nodes remain. 
The remaining node(s) would be the root of minimum height tree.
```
    def findMinHeightTrees(self, n, edges):
        if not edges: return [0]
        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        q = []
        vis = set()
        for i, row in graph.items():
            if len(row) == 1:
                q.append(i)
        n = len(graph)
        while n > 2:
            newq = []
            for i in q:
                j = graph[i].pop()
                graph[j].remove(i)
                n -= 1
                if len(graph[j]) == 1:
                    newq += j,
            q = newq
        return q
```

**329. Longest Increasing Path in a Matrix**
First, build a graph out of the matrix elements, then topological sort it. Record the number of layers.
```
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0
        N = len(matrix)
        M = len(matrix[0])
        larger = collections.defaultdict(int)
        smaller = collections.defaultdict(list)
        for i in range(N):
            for j in range(M):
                for I, J in [(i-1, j),(i+1, j),(i, j-1),(i, j+1)]:
                    if 0 <= I < N and 0 <= J < M and matrix[I][J] > matrix[i][j]:
                        larger[(i, j)] += 1
                        smaller[(I, J)].append((i, j))
        deg0 = [(i, j) for i in range(N) for j in range(M) if not larger[(i,j)]]
        cnt = 0
        while deg0:
            cnt += 1
            newdeg0 = []
            for i, j in deg0:
                for I, J in smaller[(i ,j)]:
                    larger[(I, J)] -= 1
                    if larger[(I, J)] == 0:
                        newdeg0.append((I, J))
            deg0 = newdeg0
        return cnt
```

Another way for topological sort is DFS. 

The post order visit would always put a root **after** its children. So a post-order visit of DFS should give us a order. 

Starting from every possible roots (whose in-degrees are zeros), we keep the maximum post-visiting time (MPT) of each node (if a node has been visited before with smaller MPT, then store the larger MPT). 

```
# construct graph here

def dfs(root):
    for kid in graph[root]:
        if not kid in vis:
            vis.add(kid)
            dfs(kid)
        MPT[root] = max(MPT[kid] + 1, MPT[root])

# for each node x with zero in-degree
#     dfs(x)
```
It ensures that the root's MPT would higher than the children's MPT. So you have one total order here.


