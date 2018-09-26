"""
93. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.

Example
Given binary tree A = {3,9,20,#,#,15,7}, B = {3,#,20,15,7}

A)  3            B)    3
   / \                  \
  9  20                 20
    /  \                / \
   15   7              15  7
The binary tree A is a height-balanced binary tree, but B is not.

"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    NOT_BALANCED = -1
    def isBalanced(self, root):
        return self.maxDepth(root) != self.NOT_BALANCED

    def maxDepth(self, root):
        if root is None:
            return 0

        # divide
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # conquer
        if left == self.NOT_BALANCED or right is self.NOT_BALANCED:
            return self.NOT_BALANCED
        if abs(left - right) > 1:
            return self.NOT_BALANCED
        return max(left, right) + 1


from BinaryTree.BinaryTreeUtil import BinaryTree
A = "{3,9,20,#,#,15,7}"
B = "{3,#,20,15,7}"
rootA = BinaryTree().deserialize(A)
rootB = BinaryTree().deserialize(B)

s = Solution()
print("Tree A's depth =", s.maxDepth(rootA))
print("Tree B's depth =", s.maxDepth(rootB))
