# Binary Search

## Basics
For complicated problems, you can call
* Python `bisect.bisect_right(s, ele)` 
* C++ `upper_bound(s.begin(), s.end(), ele)`
as a sub-procedure to do binary search. 

**Note** the difference of Python `bisect_right` vs. `bisect_left` is the same as C++ `lower_bound` vs. `upper_bound`.

`bisect_right` and `upper_bound` return what ***comes after (to the right of) any existing entries.***

If needed, you can customize your own binary searching. Here, you need to identify the style suits your problem better
```
  array.sort()
  l, r = 0, len(array) # NOTE never try array[r] in this case
  while l < r:
    mid = (l + r) // 2
    if array[mid] >= target: # NOTE when not target found,
                             # equal make sure search ending up with an element GREATER than target.
      r = mid
    else:
      l = mid + 1
  # NOW, l=r and array[r]==target
  return l
```
The first style solves most problems, while another style allows access to `array[r]`.
Useful for problem like "min element in rotated array".
```
  array.sort()
  l, r = 0, len(array) - 1 
  while l <= r:
    mid = (l + r) // 2

    if array[mid]==target:
      return mid # return when found target

    # NOTE you can access array[r] in this case, useful for problem like "min element in rotated array"

    if array[mid] > target:
      r = mid - 1
    else:
      l += mid + 1 

  # NOW, l=r+1 and target is not found
  return l
```

## Balanced BST
To keep a binary search tree balanced, it should be implemented as Red-Black tree, AVL tree or even skipping lists (probablistics) to maintain the similar heights of the branches sharing the same parent.

**LC 220. Contains Duplicate III**
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between `nums[i]` and `nums[j]` is at most t and the absolute difference between i and j is at most k.

Due to the lack of equivalent container, Python code needs to use Buckets (using collections.OrderedDict). 
C++ and Java are good for this problem thanks to `TreeSet<Integer>` (Java) and `set<long>` (C++).

C++ solution:
```
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        set<long> win;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > k) win.erase(nums[i - k - 1]);
            auto lower = win.lower_bound((long)nums[i] - t);
            
            # If *lower == nums[i] - t, then almost duplicate due to the lower bound
            # Since *lower >= nums[i] - t, so if *lower < nums[i] + t, 
            # then almost duplicate due to the upper bound
            if (lower != win.end() && abs(*lower - nums[i]) <= t) return true;
            win.insert(nums[i]);
        }
        return false;
    }
```

## More advanced
Binary search is a universal treatment for problems with **monotonic solutions**. The KEY is to identify the monotonic natural of these problems. Usually, if the solution is among a ordered list, the answer would be `Yes` before a certain number and `N` after a certain number. And you job to find the last `Y` or the first `N`.
```
1 2 3 4 5 6 7
Y Y Y N N N N
```
It is usually fast to check the correctness of your solution. So you can binary-search the solution, if wrong, just jump to the middle one.

**"410. Split Array Largest Sum"**: given the largest sum, you can check if spliting the array into k subarrays are possible in `O(n)` time.

**"786. K-th Smallest Prime Fraction"**: given the smallest prime fraction, you can check if there are `K` pairs whose prime fraction is smaller than the given value in `O(n)` time.  

**"373. Find K Pairs with Smallest Sums"**: given the smallest sum, you can check if there are `K` pairs whose sum is smaller in `O(n)` time.

Other problems:
* LC774 Minimize Max Distance to Gas Station
* LC378 Kth Smallest Element in a Sorted Matrix
* LC668 Kth Smallest Number in Multiplication Table
* LC719 Find K-th Smallest Pair Distance

On the other hand, Priority Queue can be used for many of such problems. Details see this post <https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378>.

## Some details about `bisect_right` and `bisect_left`
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

## Some thinking about the binary search "space"

**LC300. Longest Increasing Subsequence**
Given an unsorted array of integers, find the length of longest increasing subsequence.

Natually, we would keep a sorted list of the previous elements, and find a location to insert the new element. But indeed, it is not easy to see the binary search solution at the first glampse.

The key is to think about the solution space that we do NOT need to search. Like in the two-pointer problems, a certain set of solutions are inferior than the solutions we have searched. So we just skip them to save time.

```
INPUT:  1 3 5 4 2
              ^
Before: 1 3 5 (replace 5 by 4)
After:  1 3 4

INPUT:  1 3 5 4 2
                ^
Before: 1 3 4
After: ??
```

When 4 comes in, 5 can be replaced, because 134 has same length as 135, but with 4 at the end is better for future match. During the search time, 5 is skipped to save time.

However, when 2 comes in, where should we put it? Replace 3 and 4?? No, we can not compare 134 or 12 now. So we should keep them both. It means we should keep 1, 12, 134. 

We keep a list of ending points for longest increasing subsequences (LIS) of length 1, 2, .... When a new number comes in, we locate the number it can replace by binary search or just append it as the end of a new LIS.

```
int lengthOfLIS(vector<int>& nums) {
    vector<int> res;
    for(int i=0; i<nums.size(); i++) {
        auto it = std::lower_bound(res.begin(), res.end(), nums[i]);
        if(it==res.end()) res.push_back(nums[i]);
        else *it = nums[i];
    }
    return res.size();
}
```

**LC862. Shortest Subarray with Sum at Least K** Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

At first glampse, we look for a pair of `B[i]`, `B[j]` where `sum(A[j]~A[i-1]) = B[i] - B[j] > K` and minimize `i - j`.

Given `B[i]`, we find `B[j]` which is smaller than `B[i]-K`. And among all these `j`s, we want the max one. It is to find the max of the `******` part.

```
index j < i1 with an increasing order of B[j]
|----------------|
          B[i1]
          V
*****######.....     <--- B[i2] (the new input i2 > i1)
  ^  ^
  |  B[i1]-K
  |
 B[i2] - K, skip as i2 - max(***) > i1 - max(*****)
 
* for B[j] < B[i1] - K
. for B[j] > B[i1]
```

The key is still to think about the solution space that we do NOT need to search. 

* For all `******` part, if there is some `i2>i1` s.t. `B[i2] < B[i1]`, then those `B[j] < B[i2] - K` is a subset part, but for these `j`s, `i1 - j` < `i2 - j`. It is not necessary to consider such `B[j]` for `i2`. On the other hand, If `B[i2] > B[i1]`, we just need to consider the `j`s in `####....` part for `i2`.

* The `j`s in `....` part are worse than `i1`, because `B[i1]` is smaller than `B[j]` and `i1` is closer to `i2`. Skip them too.

So essentially, only the `#####` part is worth searching. All the other parts are irrelavent. A deque fits our purpose for poping the `****` and `....` part as `B[i2]` comes in.





