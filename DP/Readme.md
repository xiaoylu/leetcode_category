## Dynamic Programming
1. Save the memory cost whenever possible
**LC 64. Minimum Path Sum**
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
and
```
        # 174. Dungeon Game
        if not dungeon: return 0
        n, m = len(dungeon), len(dungeon[0])
        memo = [2**31] * (m-1) + [1]
        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                memo[j] = max(1, min(memo[j:j+2])-dungeon[i][j])
        return memo[0]
```
Yes, we can always use standard DP, but actually one row memo would satisfy the needs.
Because
```
        # A B  C    This is the new row memo
        #  /  /
        # a b c     This is the previous row memo
        #           You update A using a and B
```
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
