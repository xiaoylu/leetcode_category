# UnionFind

To achieve the iterated `O(log* n)` time complexity, we need to 
* Path Compression which flatten the tree
```
    def find(parent, i):
        if parent[i] != i:
            parent[i] = find(parent, parent[i])
        return parent[i]
```
* Union by Rank
```
    def union_by_rank(rank, parent, i, j):
        pi, pj = find(parent, i), find(parent, j)
        if rank[pi] < rank[pj]: parent[pi] = pj
        elif rank[pj] < rank[pi]: parent[pj] = pi
        else:
            parent[pi] = pj
            rank[pj] += 1
```
The proof of time complexity is about showing there are at most `n/2^r` nodes with rank `r` 
because the branch rooted by rank-r node has at most `2^r` nodes.

**LC 685. Redundant Connection II**

[Good solution]<https://leetcode.com/problems/redundant-connection-ii/discuss/108045/C++Java-Union-Find-with-explanation-O(n)>

