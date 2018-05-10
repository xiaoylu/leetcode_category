## Notes
1. Fully exploit the order of your input:
Some questions ask for the maximum sth. while the input is somehow sorted.
You can use the ordering of sorted input.
For example:
```
    # Leetcode 720: longest word with the smallest lexicographical order. 
    # NOTE: lexicographical order is ensured by the sort!
    words.sort()
    ret = ''
    tmp = set([''])
    for word in words:
        if word[:-1] in tmp:
            if len(word) > len(ret):
                ret = word
            tmp.add(word)
    return ret
```
And
* Problem 745 Prefix and Suffix Search - latter word has larger weight
* Problem 332, return the itinerary that has the smallest lexical order 
```
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]: # sort the tickets so for the same src, dst is sorted reversely here.
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]
```
 
