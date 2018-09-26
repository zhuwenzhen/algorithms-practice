"""
LeetCode 501. Find Mode in Binary Search Tree

Given a binary search tree (BST) with duplicates,
find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nums = self.inorder(root)
        if not nums:
            return []
        if len(nums) == 1:
            return nums

        freqTable = Counter(nums)
        res = []
        mostFreq = freqTable.most_common(1)[0][1]
        for key, freq in freqTable.items():
            if freq == mostFreq:
                res.append(key)
        return res

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

from BinaryTree.BinaryTreeUtil import BinaryTree
data = "[2,#,3,#,4,#,5,#,6]"
data2 = "{3,1,20,#,#,15,23}"
root = BinaryTree().deserialize(data)
s = Solution()
print(s.inorder(root))
print(s.findMode(root))