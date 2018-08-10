# Topological Sort
To find out the order of nodes in a DAG, remove the node with in-degree/out-degree ZERO (or degree ONE in undirected graph such as tree) iteratively,
update the degree of other node pointing to the removed node.
Keep doing this you will obtain a topological order

**310. Minimum Height Trees**
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

Another way for topological sort is DPS. The post order visit would always put a root **after** its children. Starting from different root, we keep the maximum post-visiting time (MPT) of each node (if a node has been visited, then store the larger one). It ensures that the root's MPT would higher than the children's MPT. So you have one total order here.


