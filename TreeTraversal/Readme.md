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

Note that you should push the visited node (while keep going left) into the stack. So the elements in the stack are the same when call DFS recursively.

Whenever you pop up an element, its left branch has already been explored. So go right then.

**LC 144. Binary Tree Preorder Traversal**
```
    def preorderTraversal(self, root):
        node = root
        stack, res = [], []
        while node or stack:
            while node:
                res += node.val, 
                stack += node,
                node = node.left
            node = stack.pop()
            node = node.right
        return res
  ```
  
**Simplification**:
Actually, we have a "context" every time a node gets poped up from the stack. At that moment, the variables have the same values when the recursion has returned from its children in post-order dfs.

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
  
The most difficult one might be post-order traversal. My first thought is to
* visit the left and right branches first
* visit the root

we do know when we finish exploring the left branch, (at the moment, we pop up an element), but obviously, we do NOT know when we finish visiting all the nodes in the right branch, that being said, it's unknown when the first step is done and we met the root.

The idea is that post-order is reversed pre-order (not to simply reverse the result, but we should reverse the order at every level.) So, we should put the root into the right-most position in the result, hence, we push the node to a deque from its left, and keep visiting the right branch in prior to the left branch.

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
