"""Given a singly linked list L: L0 -> L1 -> ... -> Ln-1 -> Ln,
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4,5}, reorder it to {1,5,2,4,3}.
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half2 = slow.next
        slow.next = None
        head2 = None

        while half2:
            next_ = half2.next
            half2.next = head2
            head2 = half2
            half2 = next_

        # merge head and last
        n = head
        while head2:
            head2_next = head2.next
            head_next = n.next

            n.next = head2
            head2.next = head_next

            head2 = head2_next
            n = head_next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    Solution().reorderList(head)
    print head
