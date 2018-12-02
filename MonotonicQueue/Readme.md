Monotonic Queue
===
* **LC84. Largest Rectangle in Histogram**
* **LC239. Sliding Window Maximum**
* **LC907. Sum of Subarray Minimums**, which reduces to the problem of finding the "nearest" element smaller than `A[i]` 
* [Frog Jump II](https://anthony-huang.github.io/competitiveprogramming/2016/06/06/monotonic-queue.html): K steps at most with cost `A[i]` if landing at position `i`
* And .. **Any DP problem where `A[i] = min(A[j:k]) + C` where `j < k <= i`** LOL!


Sliding max/min window.
===
Problem: return all the max elements in the sliding window.

Key observation: Given input array `A`, when `A[l] < A[r]` for `l < r`, then `A[l]` should never be retuned as the sliding max, if `A[r]` has entered the sliding window.

So we maintain a monotonic array with index increasing, and value **Decreasing**.

> `[3, 1, 4, 3, 8] => [3], [3, 1], [4], [4, 3], [8]` 

The head of the increasing queue is the sliding max!


Codeforces 487B Strip
===

One extreme case is (Codeforces 487B Strip)[http://codeforces.com/contest/487/problem/B]

题意：给你一个数组，现在让你分割这个数组，要求是数组每一块最少 L 个数  且 每一块中  极值 不超过 s

(Multiset C++ solution)[https://www.cnblogs.com/zyue/p/4360175.html]


487B - Strip
We can use dynamic programming to solve this problem.

Let f[i] denote the minimal number of pieces that the first i numbers can be split into. g[i] denote the maximal length of substrip whose right border is i(included) and it satisfy the condition.

Then `f[i] = min(f[k]) + 1`, where `i - g[i] ≤ k ≤ i - l`.

We can use monotonic queue to calculate g[i] and f[i]. And this can be implemented in `O(n)` !!!

We can also use sparse table to solve the problem, the time complexity is O(n logn).

```
from collections import deque

# f[i] = min(f[k]) + 1 for g[i] - 1 <= k <= i - l
# [g[i], i] is a valid seg
# sliding window of max/min elements

def find(N, S, L, A):
    big, small = deque(), deque()

    F = [N + 1] * N
    Fsmall = deque()

    j = 0
    for i, n in enumerate(A):
        # insert (i, n)
        while big and big[-1][1] <= n:
            big.pop()
        big.append((i, n))
        while small and small[-1][1] >= n:
            small.pop()
        small.append((i, n))

        # increment j until max-min <= S
        while j <= i and big and small and big[0][1] - small[0][1] > S:
            while big and big[0][0] <= j: big.popleft()
            while small and small[0][0] <= j: small.popleft()
            j += 1

        # [j,i] is the longest segment now
        # j - 1 <= k <= i - L
        if i >= L:
            # insert i-L
            while Fsmall and Fsmall[-1][1] >= F[i - L]:
                Fsmall.pop()
            Fsmall.append((i-L, F[i - L]))

        if j == 0 and i - j + 1 >= L:
            F[i] = 1
        else:
            # remove elements before j-1
            while Fsmall and Fsmall[0][0] < j - 1:
                Fsmall.popleft()
            if Fsmall:
                F[i] = min(F[i], Fsmall[0][1] + 1)

    return F[-1] if F[-1] <= N else -1


if __name__ == "__main__":
    N, S, L = (int(_) for _ in raw_input().split(' '))
    A = [int(_) for _ in raw_input().split(' ')]
    print find(N, S, L, A)
```

LC 375. Guess Number Higher or Lower II
---
I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

Say we select `k`, then `dp[l][k-1]` is the cost of the left remaining segment and `dp[k+1][r]` is the cost of the right.

> `dp[l][r] = max(dp[l][k-1], dp[k+1][r]) + k` for `l < k < r`

As `k` increase, `dp[l][k-1] + k` goes down, `dp[k+1][r] + k` grows up.
When `dp[l][k0-1] >= dp[k0+1][r]` for the first `k = k0`, we just need to compare
`dp[l][k0-1] + k0` with `dp[k+1][r] + k` for `k < k0`.

As a sub-routine, we need to find `dp[k+1][r] + k` for `k < k0` here. This is what Monotonic Queue does in `O(1)` time.

[O(1) time to find sliding minimum of the first `k0` elements!!](https://artofproblemsolving.com/community/c296841h1273742)
