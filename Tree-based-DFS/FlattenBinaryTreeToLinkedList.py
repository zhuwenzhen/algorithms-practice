"""
453. Flatten Binary Tree to Linked List
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Example
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
Challenge
Do it in-place without any extra memory.
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    lastNode = None
    def flatten(self, root):
        if root is None:
            return
        if self.lastNode is not None:
            self.lastNode.left = None
            self.lastNode.right = root

        self.lastNode = root
        right = root.right
        self.flatten(root.left)
        self.flatten(right)