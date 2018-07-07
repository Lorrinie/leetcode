class ListNode:
    """Defination for singly-linked list"""
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        return the sum of two numbers, and these numbers are stored in reverse order of listnode
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        root = result = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            result.next = ListNode(val)
            result = result.next
        return root.next