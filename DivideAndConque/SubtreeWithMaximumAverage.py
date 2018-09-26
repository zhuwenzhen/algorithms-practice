"""
597. Subtree with Maximum Average
Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

Example
Given a binary tree:

     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2
return the node 11.
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    res = None
    max_avg = 0

    def findSubtree2(self, root):
        self.helper(root)
        return self.res

    def helper(self, node):
        if node is None:
            return 0,0

        # divide
        left_sum, left_size = self.helper(node.left)
        right_sum, right_size = self.helper(node.right)

        sum = left_sum + right_sum + node.val
        size = left_size + right_size + 1

        avg = float(sum * 1.0 / size)

        if self.res is None or avg > self.max_avg:
            self.res = node
            self.max_avg = avg
        return sum, size

from BinaryTree.BinaryTreeUtil import BinaryTree
data = "{1,-5,11,1,2,4,-2}"
root = BinaryTree().deserialize(data)

s = Solution()
node = s.findSubtree2(root)
print(node.val)