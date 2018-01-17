"""Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return self.val


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.min_stack = self._init_min_stack()

    def _traverse(self, node):
        if node.right:
            for other in self._traverse(node.right):
                yield other
        yield node
        if node.left:
            for other in self._traverse(node.left):
                yield other

    def _init_min_stack(self):
        if not self.root:
            return []
        min_stack = []
        for node in self._traverse(self.root):
            min_stack.append(node.val)
        return min_stack

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.min_stack)

    def next(self):
        """
        :rtype: int
        """
        return self.min_stack.pop()


# Your BSTIterator will be called like this:
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    print v
