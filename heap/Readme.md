## Notes
1. Top-K algorithm: pop the extra element AFTER you insert one
2. Define custom comparator
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
