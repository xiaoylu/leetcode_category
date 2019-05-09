Wavelet Tree
===

What Wavelet Tree can do?
---

Return the number of elements in subarray A[L:R] that
  * Smaller than x
  * or equal to x
  * or being the k-th smallest

in log(N) time

Binary Tree
---
[Post by Rachit Jain](http://rachitiitr.blogspot.com/2017/06/wavelet-trees-wavelet-trees-editorial.html)
[Paper](https://users.dcc.uchile.cl/~jperez/papers/ioiconf16.pdf)

Wavelet tree is a binary tree in which every node is associated with a sub-sequence of the input array.

The root is associated with the input array itself. Like quick sort, the elements `<=mid` are then assigned to the left kid, 
while the element `>mid` are assigned to the right kid. 

After the split, the elements in each sub-sequence keep their original relative order.

Each tree node stores `b[i]` which indicates the number of elements in A[:i] assigned to the left kid.

So `i - b[i]` is the number of elements in `A[:i]` which gets assigned to the right kid.

> For example, root is associated with `A=[1,3,2,5,2]`. If `mid = 2`, then
> `leftkid = [1,2,2]`
> `rightkid = [3,5]`
> thus, for the root node,
> `b=[0,1,1,2,2,3]`

Query
---

Find the K-th element in A[L:R]
* `b[R] - b[L]` is the number of elements in A[L:R] assigned to the left kid of the root
   * if `K > b[R] - b[L]`, go to left kid
   * else, go to right kid

number of occurence of x in A[L:R]
* if `x <= mid`, go left; else go right.





