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
    def merge_sort(self, node):
        if not node or not node.next:
            return node

        slow = node
        fast = node.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node1 = node
        node2 = slow.next
        slow.next = None

        left = self.merge_sort(node1)
        right = self.merge_sort(node2)
        result = self.merge(left, right)
        return result

    def merge(self, node1, node2):
        head = tail = ListNode(None)
        while node1 and node2:
            if node1.val < node2.val:
                tail.next = node1
                tail = tail.next
                node1 = node1.next
            else:
                tail.next = node2
                tail = tail.next
                node2 = node2.next
        tail.next = node1 or node2
        return head.next

    def quick_sort(self, node):
        if node and node.val is None:
            node = node.next

        if not node:
            return ListNode(None)

        if node and not node.next:
            return node

        p = node.val
        l_dummy = l_tail = ListNode(None)
        e_dummy = e_tail = ListNode(None)
        g_dummy = g_tail = ListNode(None)

        while node:
            next_ = node.next
            node.next = None
            if node.val < p:
                l_tail.next = node
                l_tail = l_tail.next
            elif node.val > p:
                g_tail.next = node
                g_tail = g_tail.next
            else:
                e_tail.next = node
                e_tail = e_tail.next

            node = next_

        l_dummy = self.quick_sort(l_dummy)
        g_dummy = self.quick_sort(g_dummy)

        head = tail = ListNode(None)
        tail = self._concatenate_to_tail(l_dummy, tail)
        tail = self._concatenate_to_tail(e_dummy, tail)
        self._concatenate_to_tail(g_dummy, tail)

        return head.next

    def _concatenate_to_tail(self, dummy, tail):
        while dummy:
            if dummy.val is None:
                dummy = dummy.next
            if dummy is None:
                break
            tail.next = dummy
            dummy = dummy.next
            tail = tail.next
        return tail

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        return self.quick_sort(head)


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(0)

    result = Solution().sortList(head)
    print head
    print result
