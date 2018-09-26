"""
376. Binary Tree Path Sum
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes.

Example
Given a binary tree, and target = 5:

     1
    / \
   2   4
  / \
 2   3
return

[
  [1, 2, 2],
  [1, 4]
]
"""

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        result = []
        path = []
        self.dfs(root, path, result, 0,  target)

        return result

    def dfs(self, root, path, result, len, target):
        if root is None:
            return
        path.append(root.val)
        len += root.val

        if root.left is None and root.right is None and len == target:
            result.append(path[:])

        self.dfs(root.left, path, result, len, target)
        self.dfs(root.right, path, result, len, target)

        path.pop()