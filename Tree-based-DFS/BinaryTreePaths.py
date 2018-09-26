"""
480. Binary Tree Paths
Given a binary tree, return all root-to-leaf paths.

Example
Given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

[
  "1->2->5",
  "1->3"
]
"""
from BinaryTree.BinaryTreeUtil import BinaryTree

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    # Method 1: Traversal
    def binaryTreePaths(self, root):
        # write your code here
        res = []
        if root is None:
            return res
        self.helper(root, str(root.val), res)
        return res

    def helper(self, node, path, res):
        if node is None:
            return

        # If this is leaf node / recursion's exit
        if node.left is None and node.right is None:
            res.append(path)
            return

        if node.left is not None:
            new_path = path + "->" + str(node.left.val)
            self.helper(node.left, new_path, res)

        if node.right is not None:
            new_path = path + "->" + str(node.right.val)
            self.helper(node.right, new_path, res)

    # Method 2: Divide and Conquer
    def binaryTreePathsDC(self, root):
        paths = []
        if root is None:
            return paths

        leftPaths = self.binaryTreePathsDC(root.left)
        rightPaths = self.binaryTreePathsDC(root.right)

        for path in leftPaths:
            paths.append(str(root.val) + "->" + path)

        for path in rightPaths:
            paths.append(str(root.val) + "->" + path)

        # root is a leaf
        if len(paths) == 0:
            paths.append(str(root.val))
        return paths

data = "{1,2,3,4,5,6,7}"
root = BinaryTree().deserialize(data)

data2 = "{1,2,3,#,5}"
root2 = BinaryTree().deserialize(data2)
s = Solution()
print(s.binaryTreePathsDC(root))