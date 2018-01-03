"""Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""
import unittest


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_symmetric_subtrees(self, root1, root2):
        if not (root1 or root2):
            return True
        if not root1 and root2:
            return False
        if not root2 and root1:
            return False

        return (root1.val == root2.val and
                self.is_symmetric_subtrees(root1.left, root2.right) and
                self.is_symmetric_subtrees(root1.right, root2.left))

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.is_symmetric_subtrees(root.left, root.right)


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.sut = Solution()

    def test_return_true_for_symmetric_bst(self):
        t = TreeNode(1)
        t.left = TreeNode(2)
        t.right = TreeNode(2)
        t.left.left = TreeNode(3)
        t.left.right = TreeNode(4)
        t.right.left = TreeNode(4)
        t.right.right = TreeNode(3)

        is_symmetric = self.sut.isSymmetric(t)

        self.assertTrue(is_symmetric)

    def test_return_false_for_asymmetric_bst(self):
        t = TreeNode(1)
        t.left = TreeNode(2)
        t.right = TreeNode(2)
        t.left.left = TreeNode(None)
        t.left.right = TreeNode(3)

        t.right.left = TreeNode(None)
        t.right.right = TreeNode(3)

        is_symmetric = self.sut.isSymmetric(t)

        self.assertFalse(is_symmetric)


if __name__ == '__main__':
    unittest.main()
