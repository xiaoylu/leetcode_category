Greedy Algorithm - Top K
===

Problem: given array `A`, return the `K` elements with max sum, i.e. the top-K elements.

First Intuition: sort `A`, return the largest `K` elements.

Key Observation: **The sequence of top-`K` elements does not matter**. We can avoid the time for sorting. 
Just replace the min element in the current top-`K` when new element comes in.

Python Solution:

```
def topK(A):
    Q = []
    for a in A:
        if len(Q) < K: 
            heapq.heappush(Q, a)
        else:
            if Q[0] < a:
                heapq.heappop(Q)
                heapq.heappush(Q, a)
    return Q
```

Understanding this problem from the view of Dynamic Programming (DP):

* Given the top-K elements within `[0, i]`
    * if `i` is not in the final top-K
        * we need top-K elements within `[0, i-1]`
    * if `i` is in the final top-K 
        * we just need top-`K-1` elements within `[0, i-1]`
            * note that the top-`K-1` within `[0, i-1]` must be a set of top-K within `[0, i-1]`
            * i.e. `top-K == top-(K-1) + the k-th largest element`
            * so, replace the ``the k-th largest element'' of top-K within `[0, i-1]` by `A[i]`

Follow-up: Non-overlapping Top-K
---

Given an array `A`, return the `K` elements with max sum, which are at least `w` elements away from each other.

For example, `K = 3, w = 2, A = [3, 7, 9, 2, 5] ==> [3,9,5]`; here `[7,9,5]` is invalid because `7`,`9` are adjacent. 

Idea: 

keep `w` heaps storing the top-K within range `A[:i+1]`, ..., `A[:i+w]`  

when `A[i+w]` comes in, replace min element in the **first heap corresponding to `A[:i+1]`**.

then make this heap the last heap.

Deal with `A[i+w+1]` and the next heap corresponding to `A[:i+2]`, so on so forth.



LC 630. Course Schedule III
---

Each course has length `t` and closed on `d`-th day. One must take courses one-by-one before their closing date.

Given `n` online courses represented by pairs `(t,d)`, return the maximal number of courses that can be taken.

Key observation: 

There are two goals to achieve:
* The current ``top-K'' courses have min `sum(t_i)`.
* A course with larger `d`, smaller `t` can replace a course with smaller `d` and larger `t` without violating the closing dates.

Solution:
* arrange courses that `d` increases
* when a new course comes in, push it into the heap
* pop up courses with longest duration until `sum(t_i)` smaller than current d
* return final heap size



Relationship to Longest-Increasing-SubSequence
---

In the Top-K problems, the top-(K-1) elements are always a subset of the top-K set.
For example,
```
   [3, 7, 9, 2, 5]
K=1 .     9
  2    7  9
  3    7  9     5
```
So replacement works.


In **LC 300. Longest Increasing Subsequence**, the length-`l-1` subsequence with earlies ending time is NOT a sub-sequence of length-`l` subsequence with earlies ending time.

So replacement does NOT work, you have to store all states in DP (ending time of subsequence length `l=1,2,3,...`)



