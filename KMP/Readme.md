# KMP algorithm
The first step is to construct array `lps`. Here, `lps[i]` indicates the length of the longest proper prefix of a string which is also te suffix. Note that proper prefix can not be input string `s` itself, the length of it should be less than `len(s)`.

Suppose we extend from `ABCFAB` to `ABCFABC`, the last `C` matches the `C` in the middle, namely,
`s[lps[i-1]] == s[i]`, so we update `lps[6] = lps[6 - 1] + 1`.

However, when we extend from `ABCFABC` to `ABCFABCG`, the last `G` does not match `F` in the middle, namely,
`s[lps[i-1]] != s[i]`, we have to narrow down the searching range. 
In __ABC__F__ABC__G, we actually already know the matching `G` depending on **ABC** alone. 
The only possible match would be some suffix of **ABC** plus the `G`, which is equal to some proper prefix of **ABC**.
Of course, it depends on `lps[2]` which is ZERO. Thus, there is no such match with `G` at the end.

```
   def longest_proper_prefix_suffix(s):
        i = 1
        lps = [0] * len(s)
        l = 0
        while i < len(s):
            if s[i] == s[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l > 0:
                    l = lps[l - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
 ```
