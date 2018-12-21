2-D optimization
===

Some problems require optimization in two dimensions.

**LC857. Minimum Cost to Hire K Workers**

The optimization problem is `max(ratio) * sum(quality)` 

where `ratio` is the wage/quality ratio of workers and `quality` is their quality.

We start with the  K lowest-quality workers first. 
Each time, we use the new lowest-quality to replace the previous one with highest ratio.

**LC787. Cheapest Flights Within K Stops**

This is Dijisktra with a K-stop constraint. It is not that straight because the optimization requires two tasks:

`min(distance)` and `min(steps)`.

Dijisktra cares only about the shortest distance. It pops up the node with min distance.

However, the next node with less steps but **longer** distance should also be considered.

We create a `mark` set to identify the nodes `(steps, node)`, and push `(distance, steps, node)` into the priority queue each time.

**LC354. Russian Doll Envelopes**

Summary
---
For optimization problem with multiple tasks, we usually apply a greedy-style search:

* Sort the input by one dimension.
* Cut-and-paste (greedy algorithm) on the second dimension with help of a heap.

which make sures we skip searching all the sub-optimal states.

