Quick Sort
===
An array may have many redundant elements - we want to put elements equal to pivot in the middle 

https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/

In 3 Way QuickSort, an array arr[l:r+1] is divided in 3 parts:
* arr[l:i] elements less than pivot.
* arr[i:j] elements equal to pivot.
* arr[j:r+1] elements greater than pivot.

Dutch National Flag Algorithm:

between `low` and `mid` are the redundant elements equal to the pivot

```
    # pivot = 4
    #
    # 1 2 3 4 4 4 1 2 12 3 7 8 9
    #       ^     ^      ^
    #       low   mid    high
    #
    int mid = low; 
    int pivot = a[high]; 
    while (mid <= high) 
    { 
        if (a[mid]<pivot) 
            swap(&a[low++], &a[mid++]); 
        else if (a[mid]==pivot) 
            mid++; 
        else if (a[mid]>pivot) 
            swap(&a[mid], &a[high--]); 
    }
```

**LC 324. Wiggle Sort II**
Given an unsorted array nums, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]....`

Solution with [virtual indexing](https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing)

```
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if not nums: return []
        
        def w(i):
            return (1+2*i) % (N|1)
        
        def swap(i, j):
            nums[w(i)], nums[w(j)] = nums[w(j)], nums[w(i)]
            
        def partition(nums, l, r, x):
            i, j, k = 0, 0, r
            while j <= k:
                if x < nums[w(j)]: 
                    swap(i, j)
                    i += 1
                    j += 1
                elif nums[w(j)] < x:
                    swap(j, k)
                    k -= 1
                else:
                    j += 1
            return i, j
            
        # find the k-th "smallest" element
        def find(nums, l, r, k): 
            if l == r: return nums[w(l)]
            if k <= r - l + 1:
                x = random.randint(l, r)
                i, j = partition(nums, l, r, nums[w(x)])
                if k <= i - l:
                    return find(nums, l, i - 1, k)
                elif k > j - l:
                    return find(nums, j, r, k - (j - l))
                else:
                    return nums[w(i)]
            return float('inf')
        
        median = find(nums, 0, N - 1, (N + 1)//2)
        
        partition(nums, 0, N - 1, median)
 ```
