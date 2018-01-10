"""Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""

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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next

        if not head:
            return head

        prev = None
        n = head
        while n:
            if n.val == val:
                prev.next = n.next
            else:
                prev = n

            n = n.next

        return head

if __name__ == '__main__':
    head = ListNode(6)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    print Solution().removeElements(head, 6)
