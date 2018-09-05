# Knapsack

**LC 691. Stickers to Spell Word**

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

```
    def minStickers(self, s, t):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        mp = [Counter(w) for w in s]
        dp = {"":0}
        def find(t):
            if t in dp: return dp[t]
            res = sys.maxsize
            for i in range(len(s)):
                if mp[i][t[0]] > 0:
                    tmp = mp[i].copy()
                    r = ""
                    for j in range(len(t)):
                        if tmp[t[j]] > 0: tmp[t[j]] -= 1
                        else: r += t[j]
                    res = min(res, 1 + find(r))
            dp[t] = res
            return dp[t]
        R = find(t)
        return R if R < sys.maxsize else -1
 ```
