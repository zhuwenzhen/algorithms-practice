"""
448. Inorder Successor in BST
Given a binary search tree (See Definition) and a node in it,
find the in-order successor of that node in the BST.
If the given node has no in-order successor in the tree, return null.

Example
Given tree = [2,1] and node = 1:

  2
 /
1
return node 2.

Given tree = [2,1,3] and node = 2:

  2
 / \
1   3
return node 3.

Challenge
O(h), where h is the height of the BST.
"""
class Solution(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if root is None or p is None:
            return None

        successor = None
        while root is not None and root.val != p.val:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        if root is None:
            return None

        if root.right is None:
            return successor

        root = root.right
        while root.left is not None:
            root = root.left

        return root