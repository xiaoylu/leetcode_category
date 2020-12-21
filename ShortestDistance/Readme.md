# Shortest Distance

## Dijkstra's algorithm

The time complexity depends on how to support the operations
* **return the min key** to find the next nearest node (T1 time)
* **decrease some key** to update the distance to the neighbors of the nearest node (T2 time)

We return every vertex with min distance once, then decrease neighbors' distance along its out-going edges.

The time complexity is: `O(E T2 + V T1)`.

If you use a binary heap or BST, `T1=T2=O(log V)`
Elif you use a Fibonacci heap, `T2=O(1)` and `T1 = O(log V)`.


See <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm> for algorithm pseudo code 
and <https://en.wikipedia.org/wiki/Binary_heap> for compaison between heap implementations.

But, how to quickly finish the code in interviews? One trick is to skip the decrease key operation and just insert the value directly.
This step would increase the size of the queue from `V` to `E`, leading to `O(E log E)` time, but it simplifies your code. You should make sure the interviewee knows that you know the Fibonacci heap implementation later.

Using C++ `std::priority_queue` [DarthPrince's blog](https://codeforces.com/blog/entry/16221):
```
bool mark[MAXN];
void dijkstra(int v){
	fill(d,d + n, inf);
	fill(mark, mark + n, false);
	d[v] = 0;
	int u;
	priority_queue<pair<int,int>,vector<pair<int,int> >, less<pair<int,int> > > pq;
	pq.push({d[v], v});
	while(!pq.empty()){
		u = pq.top().second;  // the shortest distance to u
		pq.pop();
		if(mark[u])
			continue;
		mark[u] = true;
		for(auto p : adj[u]) //adj[v][i] = pair(vertex, weight)
			if(d[p.first] > d[u] + p.second){
				d[p.first] = d[u] + p.second;
				pq.push({d[p.first], p.first});
			}
	}
}
```

Note that a node might be poped up from the queue multiple times... with further distance from the source node. We eliminate them by the `mark`s.

It is quite interesting that we can skip `mark`s in the problem below:

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

## Searching states in a graph

Many problems can be viewed as a shortest distance problem. It might need some attention to realize that the essence of problem. But these problems are common in the way that:
* The process can be divided in primitive segments, which is a jump/edge in the states graph
* The goal is to transit from a starting state to some desired states.

Problems like this include:

* **LC 753. Cracking the Safe** The sequence (3 digits for example) 000,001,010,011,100,101,110,111
can be treated as the edges:
```
   10
  /   \
00     11
  \   /
    01
```
000 is a self-edge from 00 to 00, 001 is an edge from 00 to 01, so on so forth...
The essence of this problem is to find out a shortest path visiting all edges of the graph. We might visit an edge multiple times in a graph, but for our graph, there exist a Eular path visiting every edge eaxctly once because every node has out-degree TWO.

* **LC 864. Shortest Path to Get All Keys**
We consider the lock, key, start point @ as interest points. Since we won't touch the walls, the problem is to find a sequence of interests point pairs which are combined to be the final route. The state is `(keys, i, j)` where `keys` is the set of obtained keys, `i, j` is a pair of interest points. The edge goes from `(keys, i, j)` to `(keys, j, k)` if `j` is not a key; otherwise to `(keys+{j}, j, k)` if `j` is a key. The corresponding weight of an edge is the shortest distance from `j` to `k`, which can be found by BFS. So, we start with no key, and end up with all keys, the problem asks for the shortest distance in the weighted states graph.





