## Notes 
1. Sort First: nums.sort() 
2. Move `j,k` pointers for each i:
   `while (j<k): if too much: k--; elif too less: j++`
3. Check duplicates `while j<k and duplicates: j++ or k--`,`while i<len-2 and duplicates: i++` 

## 4sum
1. Reduce to n^2 x 2sum is better than n x 3sum because O(n^2 log(n)) < O(n^3)
2. Use set to avoid duplicates in results
3. Remove both 2sum keys after matching 

## 4sum II
1. No need to iterate over keys of AB sum again. Find AB[-c-d] directly. 
2. collections.Counter can make the code shorter.

## 2sum III
1. Use dict whenever possible 
2. Balancing the add/find. One operation should be O(n).

## 209.Minimum Size Subarray Sum
1. Two pointer shrink&expand, for loop to move the right pointer, while loop to move the left one

## 325. Maximum Size Subarray Sum Equals k
1. keep hash of the smallest index r s.t. hash[ sum(nums[:r]) ] = r

## 80. Remove Duplicates from Sorted Array II
1. As you modify the list in place, you can't compare nums[i] with nums[i-2]. You can only compare current value with the modified value nums[j-2].

## 228. Summary Ranges
1. r[len(r):] = n,  means r.append(n)
   but r[1:] = n,  means if not r, r=[n] elif len(r)>0: r[1] = n

## 88. Merge Sorted Array
1. In-place merge at the end of array, stop when run out of nums2  

