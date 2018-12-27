Hungarian Algorithm
===

Problem:

* Input: n workers and m tasks, worker i gets paid `cost(i, j)` to finish task j
* Output: min cost to finish all tasks

Key observation: the optimal assignment given original input is still optimal
if a number is subtracted from one row or column in the cost matrix

[blog](https://www.hackerearth.com/fr/practice/algorithms/graphs/minimum-cost-maximum-flow/tutorial/)
```
function: HungarianAlgorithm(Matrix C):
    Copy C into X
    for i from 1 to N:
        subtract elements in row(i) of X with min(row(i))
    for j from 1 to N:
        subtract elements in column(j) of X with min(column(j))
    L = minimum number of lines(horizontal or vertical) to join all 0s in X
    while L != N:
        M = minimum number among the cells that are not crossed by the lines
        Subtract M from all the cells that are not crossed by lines
        Add M to all cells that have intersection of lines
        L = minimum number of lines(horizontal or vertical) to join all 0s in X
    return FindMinCost(X,C)
```
FindMinCost does an optimal selection of s in matrix  such that  cells are selected and non of them lie in same row or column


minimum weight perfect bipartite matching
---
The minimum weight perfect bipartite matching is the minimum cost max flow problem
![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Minimum_weight_bipartite_matching.pdf/page1-330px-Minimum_weight_bipartite_matching.pdf.jpg)

Further readings
---
[Google OR tools](https://developers.google.com/optimization/assignment/simple_assignment)



