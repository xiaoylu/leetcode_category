Monotonic Queue
===
The following question can be solved by monotonic queue:
* **LC84. Largest Rectangle in Histogram**
* **LC239. Sliding Window Maximum**
* **LC739. Daily Temperatures**
* **LC862. Shortest Subarray with Sum at Least K**
* **LC901. Online Stock Span**
* **LC907. Sum of Subarray Minimums** 
* [Frog Jump II](https://anthony-huang.github.io/competitiveprogramming/2016/06/06/monotonic-queue.html): K steps at most with cost `A[i]` if landing at position `i`

In general, the following "prototype" problems can be solved by monotonic queue:

Any DP problem where `A[i] = min(A[j:k]) + C` where `j < k <= i`
---
This is a sliding max/min window problem.

Problem statement: return the max elements in a sliding window.

Key observation: Given input array `A`, when `A[l] < A[r]` for `l < r`, then `A[l]` should never be retuned as the sliding max, if `A[r]` has entered the sliding window.

So we maintain a monotonic array with index **increasing** and value **decreasing**.

For example, with sliding window of fixed length 3,
> `A = [3, 1, 4, 3, 8] => [3], [3, 1], [4], [4, 3], [8]` 
> when element `4` enters, we remove `[3, 1]` because they are on the left and smaller than `4`, no chance being chosen as the max element.

The head of the increasing queue is the sliding max!

As simple as it is, we have a sliding window of elements, 
the only unique thing here is that we can keep the elements in the window sorted. It brings great benefits because it takes O(1) to obtain the min/max element in the window.

That's why any DP problem where `A[i] = min(A[j:k]) + C` for `j < k <= i` can be solved by Monotonic Queue.

Given a element `A[i]`, find the nearest previous element larger than it
---
Given element `A[i]`, the task is to find the maximum index `j < i` such that `A[j] > A[i]`. Namely, `A[j]` is the nearest larger element on the left of `A[i]`.

Key observation: given `A[k] < A[j] > A[i]` for `k < j < i`, `A[k]` never become the **nearest** element larger than `A[i]` because of `A[j]`.

So we should have a decreasing monotonic queue here. The arrow indicates that the mapping from element on the right to the nearest element on the left larger than it. The elements in the valley are ignored.

![alt text](https://imgur.com/ZfQSOag.png)

**LC 85. Maximal Rectangle**

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Idea: convert 2D matrix to 1D height array. The task becomes **LC84. Largest Rectangle in Histogram** which is essentially "finding the index of the nearest previous value smaller than itself".

```
        if not matrix: return 0
        N, M = len(matrix), len(matrix[0])
        dp = [0] * (M + 1)
        area = 0
            
        for i in range(N):
            for j in range(M):
                # obtain the height based on each row
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0
            
            s = []
            for j in range(M + 1): # IMPORTANT: note that the last ZERO should pop out all remaining heights
                if not s: s.append(j)
                else:
                    while s and dp[s[-1]] >= dp[j]:
                        x = s.pop()
                        if s: area = max(area, dp[x]*(j - s[-1] - 1))
                        else: area = max(area, dp[x]*j)
                    s.append(j)
            
        return area
  ```

**LC862. Shortest Subarray with Sum at Least K**

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

Key observation: If we accumulate array A to obtain B, then `B[l] <= B[r] - K` indicates `sum(A[l:r]) >= K`. Given `B[r]`, the problem is equivalent to finding the **nearest** previous element `B[l]` such that `B[l] <= B[r] - K`. 

We maintain a **increasing queue** here because, given a new `B[i]`, the larger element on the left are inferior than `B[i]` as a candidate to make some future element `B[j] >= B[i] + K` (`j > i`).

One extra optimization learnt from [@lee215](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque) is that we can also pop up the element on the left side `<= B[i] - K` of the **increasing** queue because, given current element `B[i]`, if a future element `B[j] > B[i]`, then `B[j] - K` would be within the queue after the removal of such elements `<= B[i] - K`; Otherwise, if a future element `B[j] > B[i]` then it never appears in the final results.

```
        Q = collections.deque([])
        
        B = [0]
        for a in A: B.append(B[-1] + a)
            
        res = float('inf')
        for i, b in enumerate(B):
            if not Q: Q.append(i)
            else:
                while Q and B[Q[-1]] > b: Q.pop()
                while Q and B[Q[0]] <= b - K:
                    res = min(res, i - Q[0])
                    Q.popleft()
                Q.append(i)
        return res if res < float('inf') else -1
```
 
Frog Jump II
---

A Frog jumps K steps at most. It costs `A[i]` to stays at `i`.
Return the min cost to get to `N-1` from `0`

```
#K = 2
#A = [0, 3, 2, 7, 1, 4]
#cost 0  3  2  9  3
#     0
#     0  3
#     0     2
#     -     2  9
#           2  -  3        # remove 9 because 3 < 9 and it's on the right
#                 3  7
#
```

Pay attention to the two `while` loop.
```
from collections import deque
def min_cost(A, K):
    Q = deque([(0, A[0])])
    for i in range(1, len(A)):
        
        # keep sliding width == K steps
        while Q and Q[0][0] < i - K:
            Q.popleft()
            
        # remove inferior elements at the tail
        while Q and Q[-1][1] > A[i] + Q[0][1]:
            Q.pop()

        Q.append((i, A[i] + Q[0][1]))
    return Q[-1][1]
```

**LC975. Odd Even Jump**
---
Find a `j` of each `i` such that `j > i` and `A[j] = min(A[x] > A[i])` for all `x > i`.

This problem may not sound that straight-forward. But, if we sort `A` and arrange the indices by the increasing order of `A[i]` as `B`.
For example, `A=[5,2,1,3,4]`, then the indices would be `B=[2,1,3,4,0]`.

The corresponding `j` of `i` would be the **next indice in B larger than i**, which gets projected to the monotonic queue problem.


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
