Morris Traversal
===

O(N) time O(1) space tree traversal. Works for pre-, post-, in-order traversal of binary trees.

```
# We start from the input tree and end up with the input tree
# Go Down: the clock-wise shift at the first visit of each node (pre-order)
# Go Up: the anti-clockwise shift at the second visit of each node (in-order)
#
#        |    ^
#        V    |
#
#   parent
#       \
#        current
#        /    \
#      lkid   rtreeA
#      /  \
#   ltree rtreeB  
#
#        |    ^
#        V    |                # After clock-wise shift, current becomes the right kid of the right-most node rooted by lkid
#
# parent
# |
# |    lkid  <---------
# |    /  \           |
# | ltree rtreeB      |
# |         \         |
# |-------> current----        # note that current's left kid is still lkid, 
#             \                # so we can recover the original tree after Morris traversal
#            rtreeA
#
#        |    ^
#        V    |
#
```

```
current = root
while current:
  if current.left is None:
    # visit left-most node in every branch
    current = current.right
  else:
    prev = current.left
    while prev.right and prev.right != current:
      prev = prev.right
    
    if prev.right == current: # recovery, go up
      # inorder here
      prev.right = None
      current = current.right
    else:                     # visit, go down
      # pre-order here
      prev.right = current
      current = current.left
```

The post-order visit can be done in a similar fashion as in this post (https://github.com/xiaoylu/leetcode_category/edit/master/TreeTraversal/Readme.md).

