"""
给一棵二叉树，找到最长连续路径的长度。
这条路径是指 任何的节点序列中的起始节点到树中的任一节点都必须遵循 父-子 联系。
最长的连续路径必须是从父亲节点到孩子节点（不能逆序）。

595. Binary Tree Longest Consecutive Sequence
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Example
For example,

   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
"""



"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):
        self.longest = 0
        self.helper(root)
        return self.longest

    def helper(self, root):

        if root == None:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        subLongest = 1
        if root.left != None and root.val + 1 == root.left.val:
            subLongest = max(subLongest, left + 1)
        if root.right != None and root.val + 1 == root.right.val:
            subLongest = max(subLongest, right + 1)
        if subLongest > self.longest:
            self.longest = subLongest

        return subLongest