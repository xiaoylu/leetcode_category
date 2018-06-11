## Binary Search
For complicated problems, you can call
* Python `bisect.bisect_right(s, ele)` 
* C++ `upper_bound(s.begin(), s.end(), ele)`
to do binary search as a sub-procedure to solve a bigger problem. 
**Note** the difference of Python `bisect_right` vs. `bisect_left` is the same as C++ `lower_bound` vs. `upper_bound`.
***`bisect_right` and `upper_bound` return what comes after (to the right of) any existing entries.***

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

Binary search is a universal treatment for monotonic functions. The KEY is to identify the monotonic natural of the solution of these problems. Usually, if the solution is among a ordered list, the answer would be `Yes` before a certain number and `N` after a certain number. And you job to find the last `Y` or the first `N`.
```
1 2 3 4 5 6 7
Y Y Y N N N N
```
It is usually fast to check the correctness of your solution. So you can binary-search the solution, if wrong, just jump to the middle one.

* "Minimize Max Distance to Gas Station"
* "Find K-th Smallest Pair Distance"
* "K-th Smallest Prime Fraction"
