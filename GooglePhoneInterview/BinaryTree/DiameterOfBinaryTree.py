"""
1181. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # base case: Tree is empty
        if root is None:
            return 0
        # longest left subtree depth + longest right subtree depth
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return leftHeight + rightHeight

    def height(self, node):
        # Base case: tree is empty
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))


