"""Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            this_root = preorder.pop(0)
            i = inorder.index(this_root)
            root_node = TreeNode(this_root)
            root_node.left = self.buildTree(preorder, inorder[:i])
            root_node.right = self.buildTree(preorder, inorder[i+1:])
            return root_node


if __name__ == '__main__':
    preorder = [1, 2, 4, 5, 3, 6, 7, 9, 8]
    inorder = [4, 2, 5, 1, 3, 7, 9, 6, 8]
    print Solution().buildTree(preorder, inorder)
