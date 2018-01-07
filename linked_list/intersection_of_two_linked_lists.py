"""Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 ->  a2
                   \
                     c1 -> c2 -> c3
                   /
B:     b1 -> b2 -> b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

"""
import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not (headA and headB):
            return

        n = headA
        a_count = 0
        while n:
            a_count += 1
            n = n.next

        m = headB
        b_count = 0
        while m:
            b_count += 1
            m = m.next

        n = headA
        m = headB
        if a_count > b_count:
            offset = a_count - b_count
            while offset:
                n = n.next
                offset -= 1
        elif b_count > a_count:
            offset = b_count - a_count
            while offset:
                m = m.next
                offset -= 1

        while n and m:
            if n.val == m.val:
                return n

            n = n.next
            m = m.next

    def getIntersectionNode(self, headA, headB):
        if not (headA and headB):
            return

        n = headA
        m = headB

        while n and m:
            if n.val == m.val:
                return n

            if n.next is None and m.next is None:
                return

            if n.next is None:
                n = headB
            else:
                n = n.next

            if m.next is None:
                m = headA
            else:
                m = m.next


class ListsIntersectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    def test_find_intersect_node_for_lists_of_the_same_size(self):
        headA = ListNode('a1')
        headA.next = ListNode('a2')
        headA.next.next = ListNode('c1')
        headA.next.next.next = ListNode('c2')

        headB = ListNode('b1')
        headB.next = ListNode('b2')
        headB.next.next = ListNode('c1')
        headB.next.next.next = ListNode('c2')

        result = self.s.getIntersectionNode(headA, headB)
        result1 = self.s.getIntersectionNode1(headA, headB)

        self.assertEqual(result.val, 'c1')
        self.assertEqual(result1.val, 'c1')

    def test_find_intersect_node_given_lists_of_different_sizes(self):
        headA = ListNode('a1')
        headA.next = ListNode('a2')
        headA.next.next = ListNode('c1')
        headA.next.next.next = ListNode('c2')

        headB = ListNode('b1')
        headB.next = ListNode('b2')
        headB.next.next = ListNode('b3')
        headB.next.next.next = ListNode('c1')
        headB.next.next.next.next = ListNode('c2')

        result = self.s.getIntersectionNode(headA, headB)
        result1 = self.s.getIntersectionNode1(headA, headB)

        self.assertEqual(result.val, 'c1')
        self.assertEqual(result1.val, 'c1')

    def test_return_none_given_lists_with_no_intersection(self):
        headA = ListNode('a1')
        headA.next = ListNode('a2')
        headA.next.next = ListNode('c3')
        headA.next.next.next = ListNode('c4')

        headB = ListNode('b1')
        headB.next = ListNode('b2')
        headB.next.next = ListNode('b3')
        headB.next.next.next = ListNode('c1')
        headB.next.next.next.next = ListNode('c2')

        result = self.s.getIntersectionNode(headA, headB)
        result1 = self.s.getIntersectionNode1(headA, headB)

        self.assertIsNone(result)
        self.assertIsNone(result1)

    def test_return_non_given_one_list_is_none(self):
        headA = None

        headB = ListNode('b1')
        headB.next = ListNode('b2')
        headB.next.next = ListNode('b3')
        headB.next.next.next = ListNode('c1')
        headB.next.next.next.next = ListNode('c2')

        result = self.s.getIntersectionNode(headA, headB)
        result1 = self.s.getIntersectionNode1(headA, headB)

        self.assertIsNone(result)
        self.assertIsNone(result1)


if __name__ == '__main__':
    unittest.main()
