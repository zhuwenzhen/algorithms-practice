"""
900. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value,
find the value in the BST that is closest to the target.

Example
Given root = {1}, target = 4.428571, return 1.
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if root is None:
            return
        lowerBound = self.lower(root, target)
        upperBound = self.upper(root, target)

        if lowerBound is None:
            return upperBound.val
        if upperBound is None:
            return lowerBound.val
        if target - lowerBound.val > upperBound.val - target:
            return upperBound.val
        return lowerBound.val

    # lowerBound is to find the max value that is less than target
    def lower(self, root, target):
        if root is None:
            return None
        if root.val > target:
            return self.lower(root.left, target)
        else:
            lowerNode = self.lower(root.right, target)
        if lowerNode:
            return lowerNode
        return root

    # upperBound is to find the min value that is greater than target
    def upper(self, root, target):
        if root is None:
            return None
        if root.val < target:
            return self.upper(root.right, target)
        upperNode = self.upper(root.left, target)
        if upperNode:
            return upperNode
        return root