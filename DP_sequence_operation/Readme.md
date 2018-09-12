Sequence Operation (Dynamic Programming)
====

Some questions ask for the optimal stragety to operate on an input sequence, which includes:
* **LC312. Burst Balloons**
* **LC546. Remove Boxes**
* **LC488. Zuma Game**

The key to solve these problems is to reduce from a sequence `dp[i][j]` to a shorter sequence `dp[i][w]` and `dp[w+1][j]`.
But there are some tricks:


**LC312. Burst Balloons**
----

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. 
If the you burst balloon i you will get `nums[left] * nums[i] * nums[right]` coins. 
Here left and right are adjacent indices of i. 
After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

> Input: [3,1,5,8]
> Output: 167 

```
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

Suppose ballon `i` burst last. The left and right ballon at index `l` and `r` would impact it.
```
    def maxCoins(self, nums):
        #  l     i   r
        # [1 3 1 5 8 1]
        #      l i   r
        # dp[l][r] = max (. , dp[l][i] + dp[i][r] + n[l]*n[i]*n[r])
        
        if not nums: return 0
        n = [1] + nums + [1]
        N = len(n)
        dp = [[0] * N for _ in range(N)]
        for r in range(N):
            for l in range(r-2, -1, -1):
                for i in range(l+1, r): # i is neither l nor r.
                    dp[l][r] = max(dp[l][r], dp[l][i] + dp[i][r] + n[l]*n[i]*n[r])
        return dp[0][N-1]
```

**LC546. Remove Boxes**
---

Given several boxes with different colors represented by different positive numbers. 
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.

```
> [1, 3, 2, 2, 2, 3, 4, 3, 1] 
> ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
> ----> [1, 3, 3, 3, 1] (1*1=1 points) 
> ----> [1, 1] (3*3=9 points) 
> ----> [] (2*2=4 points)
```

If the sequence `i,j` can be split into non-empty left and right parts, then reduction is easy.
But if `b[i]==b[j]`, we have to consider all segments splitted by `b[i]`.

```
>     i     w1    w2    j    
> [1, 3, 2, 3, 2, 3, 4, 3, 1]
>      [*]   [*]   [*]           <== three segments for DP reduction
```

The last removal in this case could be the four 3s in [i,j]. Then DP reduces to 3 segments. Too complicated.

So, why not just consider the right most 3, and reduce one step at a time? 
We need one extra value to store the number of following 3s.

> `dp[i][j][0] = max(dp[i][w2][1] + dp[w2+1][j-1][0]`
>                   `,dp[i][w1][1] + dp[w1+1][j-1][0])`

```
    def removeBoxes(self, b):        
        if not b: return 0
        N = len(b)
        dp = [[[0] * N for j in range(N)] for i in range(N)]
        def find(i, j, k):
            if j < i: return 0
            if i == j: return (k + 1) * (k + 1)
            if dp[i][j][k] > 0: return dp[i][j][k]
            while j > i and b[j-1] == b[j]: 
                j -= 1
                k += 1
            dp[i][j][k] = find(i, j - 1, 0) + (k + 1) * (k + 1)
            for w in range(j-1, i-1, -1):
                if b[w] == b[j]:
                    dp[i][j][k] = max(dp[i][j][k], find(i, w, k+1) + find(w+1, j-1, 0))
            return dp[i][j][k]
        return find(0, N-1, 0)
  ```


