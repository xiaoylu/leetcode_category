# Regular Expression Match

The regular experssion matching problem can be abstracted as a DP problem.
* Given the wildcard `p[j] == "*"`, we can reduce the current match between `s[:i]` and `p[:j]` to sub-states:
  * We match `s[i]` with the `*` at `p[j]`, so `dp[i][j] => dp[i-1][j-1]`
  * We match `s[i]` with the `*` at `p[j]`, but remain `*`, so `dp[i][j] => dp[i-1][j]`
  * We do not match the `*`, so `dp[i][j] => dp[i][j-1]`
* Given the wildcard `p[j] == "."`, we must match it with a char at `s[i]`

**LC 44. Wildcard Matching**, implement wildcard pattern matching with support for '?' and '*'.

```
    def isMatch(self, s, p):
        if not s and not p: return True
        if not s: return len(p.replace("*", ""))==0
        N, M = len(s), len(p)
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True
        for j in range(1, M + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j-1]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if p[j - 1] == '*':
                # three cases: zero          one             duo
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        return dp[N][M]
```

**LC 10. Regular Expression Matching** implement regular expression matching with support for '.' and '*'.

* '.' Matches any single character.
* '*' Matches zero or more of the preceding element.

```
    def isMatch(self, s, p):
        if not s and not p: return True
        N, M = len(s), len(p)
        dp = [[False] * (M + 1) for _ in range(N + 1)]
        dp[0][0] = True
        for j in range(1, M + 1):
            if j >= 2 and p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        if not s: return dp[0][M]
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if j - 2 < 0: dp[i][j] = False
                    elif p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        #          empty         match one       match duo
                        dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
                elif p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False  
        return dp[N][M]       
```
