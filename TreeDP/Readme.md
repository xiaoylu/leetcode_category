Tree DP
===

Always think by rooting the sub-tree.

Often DFS visit a tree -- at post order, update state `dp[v]` of the current node `v`, using its children `u`'s state `dp[u]`.

LC543. Return the longest path between **any** two nodes in a binary tree.
---

At the post-order visit of the sub-root, return the longest path going through this sub-root.
```python
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def f(r):
            if not r: return -1
            left = f(r.left)
            right = f(r.right)
            self.ans = max(self.ans, left + right + 2)
            return max(left, right) + 1
        f(root)
        return self.ans
```

Problem: find number of different sub trees of size less than or equal to K.
---

Assume a subroot node `u` has children `v_1`, `v_2`, ... `v_n`:

- `f[v_i][k]` is the number of sub trees with `k` nodes and `v_i` as root.
- For such `u` as sub-root
  - `dp[i][j]` is the number of sub-trees rooted by `u`'s first `i` children with a total of `j` nodes.

So we have,

`dp[i][j] = sum_k ( dp[i - 1][j - k] * f[v_i][k] )`
`f[v][k] = dp[n][k]`

To save memory, we can use a rolling one-dim array to store the `dp` (rather than a two-dim matrix).

The final result is `sum_v( sum(f[v][:K]) )`.



