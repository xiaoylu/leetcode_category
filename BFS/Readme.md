## Breath First Search 
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
Using deque (Dijkstra uses a heap instead)
```
    Q = collections.deque(sources)
    explored = set()
    distance = 1
    while Q: 
        for _ in range(len(Q)):
            node = Q.popleft()
            if node in destinations: 
                return
            explored.add(node)
            for neighbour in neighborhood(node):
                if neighbour not in explored:
                    Q.append(neighbour)
        distance += 1
```
Both need to keep a visisted nodes set, both modify the list/deque inside the iterations, both check if visisted node is THE destination as the FIRST step inside the iterations. 

**Multiple sources & destinations**
The code above (both styles) can be trivially extended to multiple sources and multiple destinations case. So, don't run the algorithm for each source, you simply add the all sources to the initial list/deque.
