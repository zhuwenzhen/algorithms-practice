"""
902. Kth Smallest Element in a BST
Given a binary search tree,
write a function kthSmallest to find the kth smallest element in it.

Example
Given root = {1,#,2}, k = 2, return 2.

Challenge
What if the BST is modified (insert/delete operations)
often and you need to find the kth smallest frequently?
How would you optimize the kthSmallest routine?
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
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.k -= 1

        if self.k == 0:
            self.result = root.val
        if self.k > 0:
            self.inorder(root.right)