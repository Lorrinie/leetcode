"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # next_stack stores the next node
        p, next_stack = head, []
        while p is not None:
            # if node p has child, then it should be flatten
            if p.child is not None:
                # if p has child and next, then the next node of p should be the next node of p.child
                # so store it in next stack(may have nested children)
                if p.next:
                    next_stack.append(p.next)
                # establish the relationship of p and p.child, set p.child = None
                p.next, p.child.prev, p.child = p.child, p, None
            # if p.next is None and next_stack is not empty
            # means p should be the prev node of the last element of next stack
            if p.next is None and next_stack:
                p.next = next_stack.pop()
                p.next.prev = p
            p = p.next

        return head
