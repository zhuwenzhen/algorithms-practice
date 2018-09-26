"""
175. Invert Binary Tree
Invert a binary tree.

Example
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4
Challenge
Do it in recursion is acceptable, can you do it without recursion?
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        self.dfs(root)
    def dfs(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if (left!=None): self.dfs(left)
        if (right!=None): self.dfs(right)