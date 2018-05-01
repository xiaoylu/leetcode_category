## NOTES
1. Simplify your DP code in special cases
```
        # 64. Minimum Path Sum
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
