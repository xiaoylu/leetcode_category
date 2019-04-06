# Breath First Search 
## Basics
There are two styles. Straightforward list:
```
    bfs = [(source1,0),...,(sourceN,0)]
    for node,distance in bfs:
        if node in destinations: 
            return
        for neighbor in neighborhood(node): 
            if neighbor not in set(visisted):
                bfs += (neighbor, distance+1), 
```
Using deque (Note that Dijkstra uses a heap instead of a deque)
```
    Q = collections.deque(sources)
    vis = set()
    distance = 1
    while Q: 
        n = len(Q)
        
        for _ in range(n):
            node = Q.popleft()
            
            if node in destinations: 
                return
                
            for neighbour in neighborhood(node):
                if neighbour not in vis:
                    vis.add(neighbor)
                    Q.append(neighbor)
        distance += 1
```
Both Dijkstra and BFS need to keep a visisted nodes set, both modify the list/deque inside the iterations, both check if visisted node is THE destination as the FIRST step inside the iterations. 

**Multiple sources & destinations**
The code above (both styles) can be trivially extended to multiple sources and multiple destinations case. So, don't run the algorithm for each source, you simply add the all sources to the initial list/deque.

## Bi-directional
BFS starting from source and destination at the same time. The time complexity decreases from `O(k^d)` to `O(k^(d/2) + k^(d/2))` where `k` is the average node degree and `d` is the depth of the one-directional BFS search.

Notes:
* Check intersection at **boundry** only (all the visited nodes can be discarded)
* Use `set()` instead of `list` to store the nodes at each layer, for the convenience of checking intersection.
* Always expand from the side with fewer nodes to save time

**LC 127. Word Ladder**

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

```
    def ladderLength(self, beginWord, endWord, wordList):
        def adj_word(w):
            w2 = list(w)
            for i in range(len(w)):
                for j in range(26):
                    w2[i] = chr(ord('a') + j)
                    w2_str = "".join(w2)
                    if w2_str != w:
                        yield w2_str
                w2[i] = w[i]
        
        vis = set([beginWord, endWord])
        allword = set(wordList)
        
        if endWord not in allword: return 0
        
        # Use two sets to store the layers (instead of list)
        Q1, Q2 = set([beginWord]), set([endWord])
        
        steps = 0
        while Q1 and Q2:
            tmp = set()
            for w in Q1:
                for W in adj_word(w):
                    if W in allword:
                        # Check intersection at the boundary only!!
                        if W in Q2:
                            return steps + 2
                        if W not in vis:
                            vis.add(W)
                            tmp.add(W)
            Q1 = tmp
            steps += 1
            
            # Always expand the side with fewer nodes!!
            if len(Q2) < len(Q1):
                Q1, Q2 = Q2, Q1
        return 0
```
