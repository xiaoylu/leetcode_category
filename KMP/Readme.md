# KMP algorithm

KMP checks if a `T` is a sub-string of `S` in **linear** time.

The idea is that, if `T[:i]==S[j-i:j]` and `T[i]` fails to match `S[j]`, we do not need to re-start from matching the beginning of `T`, i.e. `T[0]` with `S[j-i+1]`. This is because we already have `T[:i] == S[j-i:j]`, we can preprocess `T[:i]` to know where to re-start then.

* Preprocessing: obtain the next matching point `b[i]` so when the attempt of matching `T[i]` fails, we roll back to `T[b[i]]` to restart the matching.

* Searching: When `T[i]` mis-matches, we roll back to `T[b[i]]` to restart.

The most important note is that `T[:b[i]]` is the longest "border" of `T[:i]`. Here, "border" is defined as the string which is both a prefix and a suffix of a string.

[Why it works?](http://www.inf.hs-flensburg.de/lang/algorithmen/pattern/kmpen.htm)

If border `r` is both suffix and prefix of `x`, then `r+a` is a "border" of `x+a`.

![alt text](http://www.inf.hs-flensburg.de/lang/algorithmen/pattern/rand2.gif)

Hence, the key is to find index `b[i]` for index `i` such that we can expand the matched string before them.

![alt text](http://www.inf.hs-flensburg.de/lang/algorithmen/pattern/rand4.gif)

where `b[i]` indicates the index of next potential match of char at `array[i]`.

The searching phase of the Knuth-Morris-Pratt algorithm is in `O(n)`. A preprocessing of the pattern is necessary in order to analyze its structure. The preprocessing phase has a complexity of O(m). Since `m <= n`, the overall complexity of the Knuth-Morris-Pratt algorithm is in `O(n)`.

A **C++** implementation of preprocessing:

Note that the `b[0]=-1`. In the worst case, we starting matching from index `b[i]=0` - matching the first char.

```cpp
void kmpPreprocess(vector<int>& array)
{
    vector<int> b(array.size());
    int i=0, j=-1;
    b[i]=j;
    while (i < array.size())
    {
        while (j>=0 && t[i]!=t[j]) j=b[j]; // retreat when no matching
        b[++i]=++j;
    }
}
```

Given the preprocessed `b`, do searching:

```cpp
void kmpSearch()
{
    int i=0, j=0;
    while (i<n)
    {
        // roll back first
        while (j>=0 && t[i]!=s[j]) j=b[j];
        i++; j++;
        
        // succeess
        if (j==m)
        {
            report(i-j);
            // roll back
            j=b[j];
        }
    }
}
```


**LC 214. Shortest Palindrome** 
---

Prepend letters at the front of a string to make a palindrome. 
What's the smallest numer of letters you need to prepend?

This question essentially asks for the longest palindrome prefix of a string. With a new string

`s = g + '|' + reverse(g)`

If a proper prefix of `s` is also a suffix, it is a prefix palindrome of `g`. So we look for the **longest** proper prefix (LPP) of `s` which is also a suffix. Notice that `|` should not appear in `g` so the LPP must be inside the `g` part before `|`.

```python
    def shortestPalindrome(self, g):
        s = g + "|" + g[::-1]
        b = [0] * (len(s) + 1)
        l, r = -1, 0
        b[r] = l
        while r < len(s):
            while l >= 0 and s[l] != s[r]: l = b[l]
            l, r = l + 1, r + 1
            b[r] = l
        return g[b[-1]:][::-1] + g
```

**LC 5. Longest Palindromic Substring** 
---
Find the longest palindromic substring in `s`. 

Test all the suffix of `s[:i]`, which is also a proper prefix of it. KMP linear time for each suffix and a total of  `O(N^2)` time.

```python
    def longestPalindrome(self, s):
        def LPS(s):
            lps = [0] * len(s)
            i, l = 1, 0
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
            return l
        ret = (1,1)
        for i in range(1, len(s) + 1):
            l = LPS(s[:i][::-1] + '|' + s[:i])
            if l > ret[1]:
                ret = (i, l)
        i, l = ret
        return s[i-l:i]
```

There exists a O(N) time algorithm called Manchester algorithm. And DP also solves the problem in `O(N^2)` time.


**LINTCODE 1365. Minimum Cycle Section**
---
Given an array of int, find the length of the minimum cycle section. ex. `[1,2,3,1,2,3]` has the longest cycle section of `[1,2,3]`, so return 2 as the minimum number of cycle sections.

Idea: input `abc abc abc` would have the longest proper prefix `abc abc` which is also a suffix. So the cycle section would be `N - b[N]` where `array[0:b[N]] == array[N-b[N]:N]`.

**C++** solution:

```cpp
    int minimumCycleSection(vector<int> &array) {
        int i = 0, j = -1, N = array.size();
        vector<int> b(N + 1, -1);
        while (i < N) {
            while (j >= 0 && array[i] != array[j]) j = b[j];    
            b[++i] = ++j;
        }
        return i - b[i];
    }
```

[Another idea](https://code.dennyzhang.com/minimum-cycle-section) is to have an array `dp[i]` storing the longest cycle length at index `i`.
When `array[i]` does not match `array[j%dp[i]]`, reset the `dp[i] = i`; otherwise `dp[i] = dp[i-1]` because repeating pattern continues.
