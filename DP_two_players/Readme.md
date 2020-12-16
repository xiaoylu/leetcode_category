DP with two players
===

There are simulation questions in which two players operate in turns, each optimizing its own goal.

Reduction rule
---
If two players' optimization goal are "symmetrical", then only one reduction rule is needed.

The input range forms a valid DP state. No need to prepare two dp table. One dp table can be used for both players because they are "symmetrical".

For example, if `dp[i][j]` is the state from `i` to `j` (inclusive-inclusive), a player can only operate on `i` or `j`.
```
dp[i][j] = max(<current gain of i> - dp[i+1][j],  <current gain of j> - dp[i][j-1])
```

LC 1690. Stone Game VII
---
Alice and Bob take turns to remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row.

```
    def stoneGameVII(self, stones: List[int]) -> int:
        L = [0] + list(itertools.accumulate(stones))
        A = [[0 for _ in range(len(stones))] for __ in range(len(stones))]
        def a(i, j):
            if i == j: return 0
            if A[i][j] == 0:
                s = L[j + 1] - L[i]
                A[i][j] = max(s - stones[i] - a(i + 1, j), s - stones[j] - a(i, j - 1))
            return A[i][j]
        return a(0, len(stones) - 1)
```
