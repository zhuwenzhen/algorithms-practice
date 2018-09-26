"""
Description
Give a binary tree, and a target number,
find all path that the sum of nodes equal to target,
the path could be start and end at any node in the tree.

Example
Given binary tree:

    1
   / \
  2   3
 /
4
and target = 6. Return :

[
  [2, 4],
  [2, 1, 3],
  [3, 1, 2],
  [4, 2]
]
"""

# https://www.jiuzhang.com/solution/binary-tree-path-sum-iii/

class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        res = []

        return res

    def dfs(self, root, target, res):
        if root is None:
            return

        path = []
        self.findSum(root, None, target, path, res)


    def findSum(self, root, father, target, path, res):
        pass