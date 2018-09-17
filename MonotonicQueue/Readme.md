Monotonic Queue
===
* **LC84. Largest Rectangle in Histogram**
* **LC239. Sliding Window Maximum**
* **LC907. Sum of Subarray Minimums**, which reduces to the problem of finding the "nearest" element smaller than `A[i]` 
* [Frog Jump II](https://anthony-huang.github.io/competitiveprogramming/2016/06/06/monotonic-queue.html): K steps at most with cost `A[i]` if landing at position `i`


Any DP problem where `A[i] = min(A[i-d1:i-d2]) + C` where `d1 > d2 >= 1`
===

This is a sliding min window.

Key observation: if `A[l] > A[r]` and `l < r`, then `A[l]` should never be the min element in any sliding widow ending with index `i >= r`.

So we just maintain a monotonic array with index increasing, and value increasing.

> `[3, 1, 4, 3, 8] => [3], [1], [1, 4], [1, 3], [1, 3, 8]` 

Codeforces 487B Strip
===

One extreme case is (Codeforces 487B Strip)[http://codeforces.com/contest/487/problem/B]

题意：给你一个数组，现在让你分割这个数组，要求是数组每一块最少 L 个数  且 每一块中  极值 不超过 s

(Multiset C++ solution)[https://www.cnblogs.com/zyue/p/4360175.html]


487B - Strip
We can use dynamic programming to solve this problem.

Let f[i] denote the minimal number of pieces that the first i numbers can be split into. g[i] denote the maximal length of substrip whose right border is i(included) and it satisfy the condition.

Then `f[i] = min(f[k]) + 1`, where `i - g[i] ≤ k ≤ i - l`.

We can use monotonic queue to calculate g[i] and f[i]. And this can be implemented in O(n)

We can also use sparse table or segment tree to solve the problem, the time complexity is  or (It should be well-implemented)

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
