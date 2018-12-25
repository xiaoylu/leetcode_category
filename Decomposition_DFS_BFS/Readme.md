Decomposition Problem using DFS/BFS
===

Some problem asks for an optimal way to decomposite the input as a "sum" of many terms

LC279. Perfect Squares
---
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

BFS solution
```
    def numSquares(self, n):
        i, f = 1, []
        while i * i <= n:
            f.append(i * i)
            i += 1
        
        bfs = [(0, n)]
        vis = set([n])
        for step, num in bfs:
            if num == 0: return step
            for sqr in f:
                if num - sqr >= 0 and num - sqr not in vis:
                    vis.add(num - sqr)
                    bfs.append((step + 1, num - sqr))
        return -1
```

DFS solution
```
    def numSquares(self, n):
        dp = {0:0}
        def dfs(num):
            if num in dp: return dp[num]
            tmp = num
            i = 2
            while i * i <= num:
                tmp = min(tmp, 1 + dfs(num - i * i))
                i += 1
            dp[num] = tmp
            return dp[num]
        
        return dfs(n)
```
Note that this DFS solution works but got TLE in Leetcode. Why? This problem asks for min number of squares, instead of a specific destination. Some paths are too long (say 471 = 1 + 1 + 1 + .. + 1, a total of 471 ones sum up) to search. So BFS is better than DFS.

LC691. Stickers to Spell Word
---

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

What is the minimum number of stickers that you need to spell out the target?

BFS solution
```
    def minStickers(self, stickers, target):
        mp = [Counter(w) for w in stickers]
        
        vis = set()
        Q = [(0, target)]
        for dist, t in Q:
            if t == "": return dist
            
            for cnt in mp:
                # As the sequence does not matter, we can force matching the first letter in target    
                if t[0] not in cnt: continue
                    
                tmp = cnt.copy()
                s = ""
                for ch in t:
                    if tmp[ch] > 0:
                        tmp[ch] -= 1
                    else:
                        s += ch
                if s not in vis:
                    vis.add(s)
                    Q.append((dist + 1, s))
        return -1
```

DFS solution
```
    def minStickers(self, stickers, target):
        mp = [Counter(w) for w in stickers]
        dp = {"":0}
        
        def dfs(target):
            if target in dp: return dp[target]
            res = float('inf')
            for cnt in mp:
                if cnt[target[0]] > 0:
                    tmp = cnt.copy()
                    s = ""
                    for l in target:
                        if tmp[l] > 0:
                            tmp[l] -= 1
                        else:
                            s += l
                    res = min(res, 1 + dfs(s))
            dp[target] = res
            return res
        
        res = dfs(target)
        if res >= float('inf'): return -1
        return res
```
BFS(260ms) is still faster then DFS(360ms).

It looks like **LC964. Least Operators to Express Number** can be solved in similar way. But there is actually a shortcut using DP there.


