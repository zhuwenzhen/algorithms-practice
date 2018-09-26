"""
87. Remove Node in Binary Search Tree
Given a root of Binary Search Tree with unique value for each node.
Remove the node with given value.
If there is no such a node with given value in the binary search tree, do nothing.
You should keep the tree still a binary search tree after removal.

Example
Given binary search tree:

    5
   / \
  3   6
 / \
2   4
Remove 3, you can either return:

    5
   / \
  2   6
   \
    4
or

    5
   / \
  4   6
 /
2
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    ans = []

    def inorder(self, root, value):
        if root is None:
            return

        self.inorder(root.left, value)
        if root.val != value:
            self.ans.append(root.val)
        self.inorder(root.right, value)

    def build(self, l, r):
        if l == r:
            node = TreeNode(self.ans[l])
            return node

        if l > r:
            return None

        mid = (l + r) / 2
        node = TreeNode(self.ans[mid])
        node.left = self.build(l, mid - 1)
        node.right = self.build(mid + 1, r)
        return node

    def removeNode(self, root, value):
        self.inorder(root, value)
        return self.build(0, len(self.ans) - 1)