# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverse(head):
    """
    reverse the given list
    :param head: the head of the list
    :return: reversed list
    """
    prev = None
    while head is not None:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev

class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        # fast and slow are used to find the middle of the list
        # the step of fast is 2, the step of slow is 1
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        # if fast is not None
        if fast is not None:
            slow = slow.next

        # move fast to the head
        fast = head
        # reverse the 2nd half of the list
        tail = reverse(slow)

        # compare the two halves
        while tail is not None:
            if fast.val != tail.val:
                return False
            fast = fast.next
            tail = tail.next

        return True
