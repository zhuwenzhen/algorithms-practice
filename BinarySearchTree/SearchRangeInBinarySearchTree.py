"""
11. Search Range in Binary Search Tree
Given two values k1 and k2 (where k1 < k2)
and a root pointer to a Binary Search Tree.
Find all the keys of tree in range k1 to k2.
i.e. print all x such that k1<=x<=k2 and x is a key of given BST.
Return all the keys in ascending order.

Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12

"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    res = []
    def searchRange(self, root, k1, k2):
        if root is None:
            return self.res
        self.helper(root, k1, k2)
        return self.res

    def helper(self, node, k1, k2):
        if node is None:
            return
        if node.val > k1:
            print("case 1, go left", node.val)
            self.helper(node.left, k1, k2)
        if node.val >= k1 and node.val <= k2:
            print("case 2", node.val)
            self.res.append(node.val)
        if node.val < k2:
            print("case 3, go right", node.val)
            self.helper(node.right, k1, k2)

from BinaryTree.BinaryTreeUtil import BinaryTree
#data = "{5, 5, 5}"
data = "{20, 8, 22, 4, 12}"
root = BinaryTree().deserialize(data)
s = Solution()
print(s.searchRange(root, 10, 22))