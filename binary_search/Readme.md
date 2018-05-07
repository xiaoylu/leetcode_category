## NOTES
1. For some hard problems, it is actually easy to validate their solutions.

Some problems which seem to very tough can actually be validated easily. This includes problems: 

**"410. Split Array Largest Sum"**: given the largest sum, you can check if spliting the array into k subarrays are possible in `O(n)` time.

**"786. K-th Smallest Prime Fraction"**: given the smallest prime fraction, you can check if there are `K` pairs whose prime fraction is smaller than the given value in `O(n)` time.  

**"373. Find K Pairs with Smallest Sums"**: given the smallest sum, you can check if there are `K` pairs whose sum is smaller in `O(n)` time.  

The solutions are actually also monotonic. So BINARY SEARCH is a good choice.

On the other hand, Priority Queue can be used for many of such problems. Details see this post <https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378>.
  
