# Iterative Tree Traversal - Pre-order, In-order and Post-order


**LC 144. Binary Tree Preorder Traversal**
**LC 94. Binary Tree Inorder Traversal**
Solution:
```
    def inorderTraversal(self, root):
        res, stack = [], []
        node = root
        while node or stack:
            # go all the way to the left, exactly what recursion inorder does
            while node:
                stack.append(node) # pre-order here
                node = node.left
            
            node = stack.pop()
            res.append(node.val)   # in-order here
            
            # then go right, exactly what recursion inorder does
            node = node.right
        return res
```

**Simplification for pre-order**

The pre-order traversal can be simplified by pushing the right kid, instead of the root, into the stack.
```
    def preorderTraversal(self, root):
        node = root
        stack, res = [], []
        while node or stack:
            while node:
                res += node.val, 
                stack += node.right, # push the right kid
                node = node.left
            node = stack.pop()
            #node = node.right # this line can be removed now
        return res
 ```
 
**Post-order** is reversed pre-order (not to simply reverse the result, but we should reverse the order at every level.) We keep visiting the right branch in prior to the left branch.

The solution would be:
* push current node into deque from its left
* go right whenever possible
* we pop up a node from stack, the right branch of this node has been fully explored
* so go left

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

**A more general solution**
Of course, we can mark a node by the times you visited it. Since every node is visited three times in DFS, `vis[node]` is set as -1 initially for the pre-order visit. Change it to 0 in the in-order visit. Finally, the post-order makes `vis[node]` 1.

Dynamically release memory of `vis` so that max memory usage is height of tree.
```
        vis, node, stack = {}, root, []
        
        while node or stack:
            while node and node not in vis:
                # do sth. in pre-order 
                vis[node] = -1
                stack.append(node)
                node = node.left
            
            if not stack: break
            node = stack[-1]
            
            if vis[node] < 0: 
                # do sth. in in-order
                vis[node] += 1
                node = node.right
            else:
                # do sth. in post-order
                vis[node] += 1
                if node.left: del vis[node.left]      #IMPORTANT: release node's kids memory here
                if node.right: del vis[node.right]    #           but not the node itself, let its parent release its memory
                stack.pop()
```        
        
## N-ary Tree
The same idea works for tree with multiple kids: 
* Pre-order: visit the left-most kid first, while pushing all its siblings into the stack from left to right, and append the current node to result
* Post-order: visit the right-most kid first, while pushing all its siblings into the stack from right to left, and push the current node to the left side of result (deque)

**LC 341. Flatten Nested List Iterator**

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list `[[1,1],2,[1,1]]`,

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: `[1,1,2,1,1]`.

```
class NestedIterator(object):

    def __init__(self, nestedList):
        # reverse the input list
        self.stack = nestedList[::-1]

    def next(self):
        # pop the one at the top
        if self.hasNext():
            return self.stack.pop().getInteger()
        return -1

    def hasNext(self):
        # keep going left, meanwhile, push the sibling into the stack, the right-most is inserted first.
        while len(self.stack) > 0 and not self.stack[-1].isInteger():
            x = self.stack.pop()
            self.stack.extend(x.getList()[::-1])
        return len(self.stack) > 0
```
