"""Given a binary tree, find the length of the longest path
where each node in the path has the same value.
This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the
number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2

Note: The given binary tree has not more than 10000 nodes.
The height of the tree is not more than 1000
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    max_ = 0
    def _subtree_traverse(self, node):
        if not node:
            return 0
        left_len = self._subtree_traverse(node.left)
        right_len = self._subtree_traverse(node.right)

        if node.left and node.val == node.left.val:
            left_len += 1
        else:
            left_len = 0

        if node.right and node.val == node.right.val:
            right_len += 1
        else:
            right_len = 0
        self.max_ = max(self.max_, right_len + left_len)
        return max(left_len, right_len)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self._subtree_traverse(root)
        return self.max_


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(4)

    print Solution().longestUnivaluePath(root)

