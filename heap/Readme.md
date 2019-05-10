Heap
===

Top-K algorithm
---

While iterating through the input array, a heap maintains the current largest K elements. 
When a new element is larger the smallest of the current top-K, insert new element into the heap, then pop up the smallest element in the heap.

**LC215  Kth Largest Element in an Array**
```
from heapq import heapreplace, heappush
class Solution:
    def findKthLargest(self, nums, k):
        h = []
        for n in nums:
            if len(h)<k:
                heappush(h,n)
            elif n>h[0]:
                heapreplace(h,n)
        return h[0]
```

The heapq is a min-heap (smallest element at `h[0]`). `heapreplace(heap, item)` pop and return the smallest item, and also push the new item. The heap size doesn’t change.

2. Define custom comparator for Python heap
```
@functools.total_ordering
class Element:
    def __init__(self, word, n):
        self.word = word
        self.n = n
    
    def __lt__(self, other):
        if self.n == other.n:
            return self.word > other.word
        return self.n < other.n
    
    def __eq__(self, other):
        return self.n==other.n and self.word==other.word
```
and `heapq.heappush(hp, (Element(word, n), word, ...))` would do the job.
