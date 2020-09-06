# Disjoint Sets Union ("UnionFind")
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

A smarter way to do this (also see C++ practive below): 
* `par[i] = j` if node j is the parent of node i;
* `par[i] = -n` if node i is the root, and node i has a total of n descendents (including itself). 

```python
    def find(self, par, i):
        if par[i] < 0: return i
        par[i] = self.find(par, par[i])
        return par[i]
    
    def union(self, par, i, j):
        i, j = self.find(par, i), self.find(par, j)
        if i == j: return
        if par[j] < par[i]: i, j = j, i
        par[i], par[j] = par[i] + par[j], i
```

To conduct `n` find operations:
---
1. No optimization: `O(n^2)`
2. Path compression alone: `O(n log n)`
3. Path compression + union by rank: `O(n log*(n))~O(n)` (iterated log can be treated as a constant)

See [wiki](https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Time_complexity):

With neither path compression (or a variant), union by rank, nor union by size, the height of trees can grow unchecked as `O(n)`, which implies that Find and Union operations will take `O(n)` time.

Using path compression alone gives a worst-case running time of `O(n log n)` for n find operations on n elements.

Using union by rank alone gives a running-time of `O(n logn)` for n operations on n elements.

Using both path compression, splitting, or halving and union by rank or size ensures that the amortized time per operation is only O(1), so the disjoint-set operations take place in essentially constant time.

The best practice (C++):
---

For each root v, `par[v]` equals the negative of number of nodes in its rooted tree.

For other nodes u, `par[u]` equals the parent.

```
int root(int v){return par[v] < 0 ? v : (par[v] = root(par[v]));}
void merge(int x,int y){	//	x and y are some tools (vertices)
        if((x = root(x)) == (y = root(y))     return ;
	if(par[y] < par[x])	// balancing the height of the tree
		swap(x, y);
	par[x] += par[y];
	par[y] = x;
}
```

Or we can even use `vector` to store the elements in the same 'set'. We merge the `vector`s. Any node can be merged at most `O(log n)` times, so the total time complexity would be `O(n logn)`.

# Directed vs Undirect graph

For undirected graph, path compression + union-by-rank ==> O(1) time find/union operation.

For directed graph, neither works because edge `(i,j)` can only have `parent[j] = i`.
Path compression will make all nodes have the very root as `parent`. 
If that's fine for the specific problem, then union-find still works.

See this problem:

## Redundant Connection

**LC 685. Redundant Connection II**

Find a redundant edge in a directed tree. The directed edge of the tree points from the parent to its kid.

[Good solution](https://leetcode.com/problems/redundant-connection-ii/discuss/108045/C++Java-Union-Find-with-explanation-O(n))

Three types of the redudant edge: 
* double-parent node, no loop (easy, remove one double-parent edge to this node)
* double-parent node, loop (remove the double-parent edges inside the loop)
* no double-parent node, loop (remove the current edges once a loop is detected)

Store the two edges pointing to the double-parent node, just remove the second edge (if exist) causing the double parents, then check
* if the tree is valid now, return the second edge as result
* elif we found a loop (by using union-find on a directed graph)
1. the first edge exist, return the first edge
2. else return the current edge causing the loop


