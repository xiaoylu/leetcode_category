# Random Sampling

<https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling>

**LC 382. Linked List Random Node** Pick a random element from a linked list.

The problem is a little ambiguous. In the interview, you should ask clearly whether the list length is unknown but static or it is unknown and dynamically changing. In the first case, you can simply precompute the length and generate random indices based on that. It is faster than the reservior sampling solution.

If the list length changes dynamically, reservior sampling is a good choice. If you are not familiar with it, check here.

```
class Solution(object):

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val
```
