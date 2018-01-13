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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # revert second half
        right = slow
        prev.next = None
        head2 = None
        while right:
            next_ = right.next
            right.next = head2
            head2 = right
            right = next_

        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next

        remainer = head or head2
        return not remainer or (remainer and not remainer.next)


if __name__ == '__main__':
    head = ListNode('a')
    head.next = ListNode('b')
    head.next.next = ListNode('c')
    head.next.next.next = ListNode('b')
    head.next.next.next.next = ListNode('a')

    print Solution().isPalindrome(head)
