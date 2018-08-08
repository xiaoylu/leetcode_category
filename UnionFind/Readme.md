# UnionFind
## `O(log* n)` time
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

## Redundant Connection

**LC 685. Redundant Connection II**

Find a redundant edge in a directed tree. The directed edge of the tree points from the parent to its kid.

[Good solution](https://leetcode.com/problems/redundant-connection-ii/discuss/108045/C++Java-Union-Find-with-explanation-O(n))

Three types of the redudant edge: 
* pointing from a node to the root (lead to a loop without double-parent node)
* pointing from a node to its ancestor (lead to a loop with double-parent node)
* pointing from a node to another branch (lead to double-parent node)
* pointing from a node to its desendent (lead to double-parent node)

Just remove the second edge (if exist) causing the double parents, then check
* if the tree is valid now, return the second edge
* elif the first edge exist, return the first edge
* else return the current edge causing loop


