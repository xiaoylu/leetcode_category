## NOTES
1. For some hard problems, it is actually easy to validate their solutions.

Some problems which seem to very tough can actually be validated easily. This includes problems: 

**"410. Split Array Largest Sum"**: given the largest sum, you can check if spliting the array into k subarrays are possible in `O(n)` time.

**"786. K-th Smallest Prime Fraction"**: given the smallest prime fraction, you can check if there are `K` pairs whose prime fraction is smaller than the given value in `O(n)` time.  

**"373. Find K Pairs with Smallest Sums"**: given the smallest sum, you can check if there are `K` pairs whose sum is smaller in `O(n)` time.  

The solutions are actually also monotonic. So BINARY SEARCH is a good choice.

On the other hand, Priority Queue can be used for many of such problems. Details see this post <https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378>.

* 373. Find K Pairs with Smallest Sums
* 378. Kth Smallest Element in a Sorted Matrix
* 668. Kth Smallest Number in Multiplication Table
* 719. Find K-th Smallest Pair Distance
* 786. K-th Smallest Prime Fraction
  
2. The difference between `bisect_right` and `bisect_left`:
Source code <https://github.com/python/cpython/blob/master/Lib/bisect.py>
```
    # bisect_left()
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        # MOVE hi in the case of equality 
        # 0 1 2 3 3 3 4 5
        #       ^
        #       hi would end up staying here when searching for 3.
        else: hi = mid
    return lo
```
`bisect_right()` is similar to `bisect_left()`, but returns an insertion point which comes after (to the right of) any existing entries of x in a.
```
    # bisect_right()
    while lo < hi:
        mid = (lo+hi)//2
        # MOVE lo in the case of equality 
        if a[mid] <= x: lo = mid+1
        # 0 1 2 3 3 3 4 5
        #             ^
        #             hi would end up staying here when searching for 3.
        else: hi = mid
    return lo
```


