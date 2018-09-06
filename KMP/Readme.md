# KMP algorithm

##[Why it works?](http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/kmpen.htm)

The border `r` is both suffix and prefix of `x`, then we just `rb` is "border" of `xa`.
![alt text](http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/rand2.gif)

Hence, the key is find `b[i]` for `i` such that we can expand the matched string before them.
![alt text](http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/rand4.gif)

## Example
The first step is to construct array `lps`. Here, `lps[i]` indicates the length of the longest proper prefix of a string which is also te suffix. Note that proper prefix can not be input string `s` itself, the length of it should be less than `len(s)`.

Suppose we extend from 'ABCFAB' to 'ABCFABC', now `i=6` and `lps[5]=2` which points to the `C` in the middle, the right-most `C` matches the `C` in the middle, so we update `lps[6] = lps[5] + 1 = 3`.

However, when we extend from 'ABCFABC' to 'ABCFABCG', the right-most `G` does not match `F` in the middle, namely,
`s[lps[i - 1]] != s[i]` with `i=7`, we have to narrow down the searching range. 
Because `lps[i-1]=lps[5]=3`, in **ABC** F **ABC** G, we actually already know the matching `G` depending on **ABC** alone. 
The only possible match would be some suffix of **ABC** plus the `G`, which is equal to some proper prefix of **ABC**.
So, it depends on `lps[2]` which is the length of such suffix of **ABC**. The above case is only possible if `s[lps[2]] == 'G'`. As `lps[2]` turns out to be ZERO, and `s[0] != 'G'`. We realise that there is no such match involving `G`. So `lps[7] = 0`.

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
                    # The tricky part, ABCFABCG ==> (since ABCF != ABCG) ==> ABCG
                    #                  0000123?       
                    #                        ^the third letter 'F' is what we check
                    #                  ABCG ==> (since A != G) ==> lps[i] is 0  
                    #                  000?
                    l = lps[l - 1]
                    # Do not increment i
                else:
                    lps[i] = 0
                    i += 1
        return lps
```

With the `lps` array, it is easy to find the palindrome prefix in a string:

**LC 214. Shortest Palindrome** Append letter in the front of a string to make it a palindrome.

This question essentially asks for the longest palindrome prefix of a string. You can create a string

`s + '|' + reverse(s)`

The longest proper prefix (LPP) of string above would be palindrome if it is also a suffix. Note `|` should not appear in `s` so the LPP would be inside `s` before `|`.
```
    def shortestPalindrome(self, s):
        def LPS(s):
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
            return lps[-1]
        i = LPS(s + '|' + s[::-1])
        return s[i:][::-1] + s
```

**LC 5. Longest Palindromic Substring** 
Find the longest palindromic substring in `s`. 

Test all the suffix of `s[:i]`, which is also a proper prefix of it. KMP linear time for each suffix and a total of  `O(N^2)` time.

```
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
JAVA

Given an array of int, find the length of the minimum cycle section.

```
    public int minimumCycleSection(int[] array) {
        // Write your code here
        int [] next = new int[array.length + 1];
        int i = 0, j = -1;
        next[0] = -1;
        while(i < array.length) {
            if(j == -1 || array[i] == array[j]) {
                i++;
                j++;
                next[i] = j;
            } else {
                j = next[j]
            }
        }
        return i - next[i];
    }
```
