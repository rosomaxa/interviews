"""
Given two binary trees and imagine that when you put one of them to cover
the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree.
The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
"""


def bfs(node):
    st = [[node]]
    while st:
        next_level = []
        this_level = st.pop()
        for node in this_level:
            yield node
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if next_level:
            st.append(next_level)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            resulting_node = TreeNode(t1.val + t2.val)

            resulting_node.left = self.mergeTrees(t1.left, t2.left)
            resulting_node.right = self.mergeTrees(t1.right, t2.right)
            return resulting_node

        return t1 or t2


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    s = Solution()
    merged = s.mergeTrees(root1, root2)
    for node in bfs(merged):
        print node.val
