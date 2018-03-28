## Notes 
1. Sort First: nums.sort() 
2. Move `j,k` pointers for each i:
   `while (j<k): if too much: k--; elif too less: j++`
3. Check duplicates `while j<k and duplicates: j++ or k--`,`while i<len-2 and duplicates: i++` 

## 4sum
1. Reduce to n^2 2sum is better than n 3sum because O(n^2 log(n)) < O(n^3)
2. Use set to avoid duplicates in results
3. Remove both 2sum keys after matching 

## 
