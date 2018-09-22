# Euler Path & Euler Circuit

Euler path is a path visiting every edge exactly once.

Euler cycle (Euler tour) is a Euler path which starts and ends on the same vertex.

A graph is called Eulerian if it has an Eulerian Cycle and called Semi-Eulerian if it has an Eulerian Path.

Given a **connected** graph, 
* Euler cycle exists if all vertices have even degree
* Euler path exists if zero or two vertices have odd degree and all other vertices have even degree

To find out the Euler path/tour, we can do a **post-order DFS while removing visited edges**

It is quite like DFS, with a little change:
```
vector E
dfs (v):
        color[v] = gray
        for u in adj[v]:
                erase the edge v-u and dfs(u)
        color[v] = black
        push v at the end of e
```
e is the answer.

**LC 332. Reconstruct Itinerary**

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 

```
    def findItinerary(self, tickets):
        graph = collections.defaultdict(list)
        
        for s, t in tickets:
            graph[s].append(t)
            
        # Visit the airports with lower lexi-order first
        for s in graph:
            graph[s] = sorted(graph[s])[::-1]
        
        def dfs(s, ret):
            while graph[s]:
                # once an edge has been visited, remove it
                # it is like mark the visited vertex in normal DFS
                # pop() is easiest way to mark edge
                t = graph[s].pop()
                dfs(t, ret)
            # Now, All out-going edges from s have been removed
            # it is time to add s into the path
            ret.append(s)
        
        ret = []
        dfs("JFK", ret)
        return ret[::-1]
```

**LC 753. Cracking the Safe**

Output a string formed by `n` letters, each letter is among `[0, 1, 2, .., k-1]`
The length-n substrings should contains all possible strings `[000, 00..1, 00..2, ...]`.
For example,
Input: n = 2, k = 2
Output: "00110" contains '00', '01', '11', '10', which are all the length-2 substrings formed by letters of '0' and '1'

The problem is to find a Euler cycle visiting all the edges in a directed graph:
* Every vertex is a possible string with a length of `n-1`.
* Every vertex has `k` out-going edges for letters `0`, `1`, ..., `k-1`.

```
    def crackSafe(self, n, k):
        curr = "0" * (n - 1)
        graph = collections.defaultdict(lambda : k - 1)
        ret = []
        def dfs(s, ret):
            t = graph[s]
            if t < 0: return
            graph[s] -= 1
            dfs( (s + str(t))[len(s) + 2 - n:] , ret)
            # Post-order here, actually pre-order also works for Euler cycle 
            # (but pre-order does NOT work for Euler path problems)
            ret.append(t)
        dfs(curr, ret)
        return curr + "".join(str(i) for i in ret[::-1])
```

Another iterative implementation: we can just record every edges of DFS, 
because no matter which route we choose, there will always be a Euler cycle,
as long as we post-pone visiting the starting vertex `000..0` here.
```
    def crackSafe(self, n, k):
        ret = curr = "0" * (n - 1)
        graph = collections.defaultdict(lambda : k - 1)
        for _ in range(k**n):
            ret += str(graph[curr])
            graph[curr] -= 1
            curr = ret[len(ret) - n + 1:]
        return ret
```
