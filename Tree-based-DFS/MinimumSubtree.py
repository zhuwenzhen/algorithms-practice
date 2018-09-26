
"""
596. Minimum Subtree
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example
Given a binary tree:

     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5
return the node 1.
"""


"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    # Version 1: Traverse + Divide and conquer
    import sys
    minVal = sys.maxsize
    result = None

    def findSubtree(self, root):
        self.helper(root)
        return self.result

    def helper(self, root):
        if root is None:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)
        sum = left + right + root.val

        if  sum <= self.minVal:
            self.minVal = sum
            self.result = root

        return sum

    # Version 2: Pure Divide and Conquer

    # def findSubtreeDC(self, root):
    #
    # def dc(self, node):
    #     if node is None:
    #         return [None, 0]
