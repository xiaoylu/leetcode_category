optimization problem with multiple goals (2-D optimization)
===

Some problems require optimization using multi-dimensional input.

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

The task wants a longest sequence with both `x` and `y` dimension **strictly** increasing.

We sort the input list of tuples by its first dimension. The problem becomes the `Longest Increasing Sequence` of finding longest increasing sequence in the second dimension.

A trick is to sorted by `(x,-y)` in case the some successive `x`s are the same.

Summary
---
For optimization problem with multiple goal, we usually apply a greedy-style search:

* Sort the input by one dimension.
* Cut-and-paste (greedy algorithm) on the second dimension with help of a heap or other tricks.

which make sures we skip searching all the sub-optimal states.

