Bellman Ford Algorithm
===
Single source shortest path with complexity of O(VE)

The naive implementation:
```
    for (int i = 0; i < V; i++) 
        dist[i]   = INT_MAX; 
        dist[src] = 0; 
    
    for (int i = 1; i <= V-1; i++) 
    { 
        for (int j = 0; j < E; j++) 
        { 
            int u = graph->edge[j].src; 
            int v = graph->edge[j].dest; 
            int weight = graph->edge[j].weight; 
            if (dist[u] != INT_MAX && dist[u] + weight < dist[v]) 
                dist[v] = dist[u] + weight; 
        } 
    } 
    
    //check for negative-weight cycles
    ...
```

A better implementation:

we can push the nodes into a [deque](https://blog.csdn.net/u014800748/article/details/44059993)
Use `inq` to mark nodes in the deque.
Push new nodes into the deque only if its dist gets "relaxed" and it's not in the deque.

```
      for(int i=0;i<n;i++)
          d[i]=INF;
      memset(inq,0,sizeof(inq));
      d[s]=0,inq[s]=1,p[s]=0,a[s]=INF;

      queue<int>q;
      q.push(s);
      while(!q.empty())
      {
          int u=q.front();q.pop();
          inq[u]=0;
          for(int i=0;i<G[u].size();i++)
          {
              Edge&e=edges[G[u][i]];
              if(e.cap>e.flow&&d[e.to]>d[u]+e.cost)//松弛操作
              {
                  d[e.to]=d[u]+e.cost;
                  p[e.to]=G[u][i];//记录父边
                  a[e.to]=min(a[u],e.cap-e.flow);//更新可改进量，等于min{到达u时候的可改进量，e边的残量}
                  if(!inq[e.to]){q.push(e.to);inq[e.to]=1;}
              }
          }
      }
```
