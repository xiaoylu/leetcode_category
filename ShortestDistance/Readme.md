# Shortest Distance

## Dijkstra's algorithm

The time complexity depends on how to support the operations
* **return the min key** to find the next nearest node (T1 time)
* **decrease some key** to update the distance to the neighbors of the nearest node (T2 time)

The time complexity is: `O(E T2 + V T1)`.

If you use a binary heap or BST, `T1=T2=O(log V)`
Elif you use a Fibonacci heap, `T2=O(1)` and `T1 = O(log V)`.


See <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm> for algorithm pseudo code 
and <https://en.wikipedia.org/wiki/Binary_heap> for compaison between heap implementations.

But, how to quickly finish the code in interviews? One trick is to skip the decrease key operation and just insert the value directly.
This step would increase the size of the queue from `V` to `E`, but it simplifies your code. But you should make sure the interviewee knows that you know the Fibonacci implement afterwards!!

**LC 787. Cheapest Flights Within K Stops**  Find the shortest path with at most `k+2` nodes

```
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(list)
        for i, j, w in flights:
            graph[i].append((j, w))
        Q = [(0, src, 0)]
        while Q:
            dist, i, k = heapq.heappop(Q)
            if i == dst: return dist
            if k <= K:
                for j, w in graph[i]:
                    heapq.heappush(Q, (dist + w, j, k + 1))
        return -1
```

The queue size is `O(E)` in the worst case because every update might insert one element into queue. The time complexity becomes `O(E log E)`. But we should eliminate the loop here. See example,

```
0----2-----3----5
 \  /       \  / 
   1          4
```
To get to 2, 0-1-2 might be shorter, say distance(0-1-2)=100, but 0-2 takes less steps, distance(0-2)=200.
However, we can go 0-2-3-4-5, but can not go 0-1-2-3-4-5, if K = 3. 
So, we should insert 0-2 into the queue.

In short, a node should be updated here if (i) shorter distance (ii) less number of steps.

The heap solution checks (i) and consider all the possible number of steps. This is also what Dijkstra does because it assumes any steps is alright. 

We can prune the search space using the second measure also. (Record the current least number of steps to reach a pop-up node, and update only if less No. of steps is found)
