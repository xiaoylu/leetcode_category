# KMP algorithm

[Why it works?](http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/kmpen.htm)

The border `r` is both suffix and prefix of `x`, then `r+a` is "border" of `x+a`.

![alt text](http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/rand2.gif)

Hence, the key is find `b[i]` for `i` such that we can expand the matched string before them.

![alt text](http://www.inf.fh-flensburg.de/lang/algorithmen/pattern/rand4.gif)

Here `b[i]` indicates the index of next potential match of `array[i]`.

## Example
The first step is to construct array `b`.

A **short** implementation is here:

Note that the `b[0]=-1`. For a char `array[i]` does not match any char, we have `b[i]=0`.
```
void kmpPreprocess()
{
    int i=0, j=-1;
    b[i]=j;
    while (i<m)
    {
        while (j>=0 && array[i]!=array[j]) j=b[j]; // retreat when no matching
        b[++i]=++j;
    }
}
```

With the `b` array, it is easy to find the palindrome prefix in a string:

**LC 214. Shortest Palindrome** 

Prepend letters at the front of a string to make a palindrome. 
What's the smallest numer of letters you need to prepend?

This question essentially asks for the longest palindrome prefix of a string. With a new string

`s = g + '|' + reverse(g)`

If a proper prefix of the `s` is also a suffix, then it is the prefix palindrome of `g`. So we are looking for the longest proper prefix of `s` which is also a suffix. Notice that `|` should not appear in `g` so the LPP would be inside the `g` part before `|`.

```
    def shortestPalindrome(self, g):
        s = g + "|" + g[::-1]
        b = [-1] + [0] * len(s)
        l, r = -1, 0
        while r < len(s):
            while l >= 0 and s[l] != s[r]: l = b[l]
            l, r = l + 1, r + 1
            b[r] = l
        return g[b[-1]:][::-1] + g
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
