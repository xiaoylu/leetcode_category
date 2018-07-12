# Iterative Tree Traversal - Pre-order, In-order and Post-order

Tree problems are easier if we traverse recursively. How about iteratively?

**LC 94. Binary Tree Inorder Traversal**
```
    def inorderTraversal(self, root):
        res, stack = [], []
        node = root
        while node or stack:
            # go all the way to the left, exactly what recursion inorder does
            while node:
                stack.append(node)
                node = node.left
            
            
            node = stack.pop()
            res.append(node.val)   # in-order part here !!
            
            # then go right, exactly what recursion inorder does
            node = node.right
        return res
```

So in your mind, the rules are
* go left whenever possible (node.left != null)
* go right when it has to (appending node itself to the result)

**LC 144. Binary Tree Preorder Traversal**
```
    def preorderTraversal(self, root):
        node = root
        stack, res = [], []
        while node or stack:
            while node:
                res += node.val, # the only difference is when to append!
                
                stack += cur,
                node = cur.left
            node = stack.pop()
            node = cur.right
        return res
  ```
  
The most difficult one might be post-order traversal. My first thought is to
* visit the left and right branches first
* visit the root

but obviously, we do not know when we finish visiting all the nodes in the right branch, or, it's unknown when the first step is done.
so we do not know when to insert the root at the second step.

The idea is to insert the root into a deque, then visit both branches. 
It makes sure that the inside the deque:
```
************ ########## R
the left     the right  the root
```
For this reason, you also need to visit the right branches first.

```
    def postorderTraversal(self, root):
        res = collections.deque()
        stack = []
        node = root
        while node or stack:
            while node:
                res.appendleft(node.val) # unlike pre-order, insert node into a deque instead of stack
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        return list(res)
```
