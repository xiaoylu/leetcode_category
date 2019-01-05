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
