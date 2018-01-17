"""Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        n = self
        result = ''
        while n:
            result += str(n.val) + ', '
            n = n.next
        return result.strip(', ')


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return

        mark = head
        for i in xrange(n):
            mark = mark.next

        if mark is None:
            return head.next

        h = head
        while mark.next:
            mark = mark.next
            h = h.next

        if h:
            h.next = h.next.next
        return head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print Solution().removeNthFromEnd(head, 2)
