## Dynamic Programming

1. Save the memory cost whenever possible

**LC 64. Minimum Path Sum** Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

The basic DP reduction is 2D
```
dp[i,j] = min(dp[i-1,j], dp[i,j-1]) + grid[i][j]
```
But actually we just need 1D vector the store the states because
```
        # A  B  C    This is the old row memo
        #    V  V
        # a->b->c   This is the mew row memo
        #           You update b using a and B
```

Python Code:
```
        if not grid: return 0
        m = len(grid[0])
        memo = [0] + [2**31] * (m-1)
        for row in grid:
            memo[0] = memo[0] + row[0]
            for j in range(m-1):
                memo[j+1] = min(memo[j:j+2]) + row[j+1]
        return memo[-1]
```

**LC 174. Dungeon Game**
A knight gains/loses health entering a room. He dies if health <= 0. Return the knight's minimum initial health to get (N, M) from (0, 0).

So reversively, we compute the min health at `(i,j)` (before gains/lose health) so the knight can reach (N, M). Obviously, `dp[N-1, M-1] = 1 - dungeon[i, j]`. The reduction rule is

```
dp[i, j] = max(1, min(dp[i+1,j],dp[i,j+1]) - dungeon[i, j] )
```

After the simplification, we get
```
        if not dungeon: return 0
        n, m = len(dungeon), len(dungeon[0])
        memo = [2**31] * (m-1) + [1]
        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                memo[j] = max(1, min(memo[j:j+2])-dungeon[i][j])
        return memo[0]
```
Yes, we can always use standard DP, but actually one row memo would satisfy the needs.

**LC 714. Best Time to Buy and Sell Stock with Transaction Fee** (and the series of stock transaction problems.)

Given the daily prices of a stock, you may buy and sell on each day (only sell after you buy, and buy after you sell).
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction `fee`.

The max profit at day `i` is
```
        dp[i] = max(dp[i-1], max(p[i] - p[j] - fee + dp[j-1], for all 0 <= j < i) ) 
```
which can be simpilified as
```
        dp[i] = max(dp[i-1], p[i] - fee + max( dp[j-1] - p[j] ) ) 
```
Let `sell = dp[i]` and `buy = max( dp[j-1] - p[j] )`, only two variables are enough for the DP.

Python Code:
```
    def maxProfit(self, prices, fee):

        sell, buy = 0, -float('inf')
        for p in prices:
            buy = max(buy, sell - p)
            sell = max(sell, buy + p - fee)
        return sell
```

2.
