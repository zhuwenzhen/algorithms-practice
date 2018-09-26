"""
Question1
Find second largest element in a binary search tree.
"""

class Solution_recursion:
    def kthLargest(self, root, k):
        c = 0
        return self.kthLargestUtil(root, k, c)

    def kthLargestUtil(self, root, k, c):
        if root is None or c >= k:
            return None

        # follow reverse in-order traversal so the largest element is visited first
        self.kthLargestUtil(root.right, k, c)
        # increment count of visited nodes
        c += 1
        # if c == k, then this is the kth largest
        if c == k:
            return root.val

        # recursion for left subtree
        self.kthLargestUtil(root.left, k, c)

class Solution:

    # QuickSelect
    def kthLargest(self, root, k):
        numOfChildren = {}
        self.countNodes(root, numOfChildren)
        return self.quickSelectOnTree(root, k, numOfChildren)


    def countNodes(self, root, numOfChildren):
        if root is None:
            return 0

        left = self.countNodes(root.left, numOfChildren)
        right = self.countNodes(root.right, numOfChildren)
        numOfChildren[root] = left + right + 1
        return left + right + 1

    def quickSelectOnTree(self, root, k, numOfChildren):
        if root is None:
            return -1

        if root.right == None:
            right = 0
        else:
            right = numOfChildren[root.right]

        if right >= k:
            return self.quickSelectOnTree(root.right, k, numOfChildren)

        if right + 1 == k:
            return root.val

        return self.quickSelectOnTree(root.left, k - right - 1, numOfChildren)

# Kth Smallest
class Solution:

    # QuickSelect
    def kthSmallest(self, root, k):
        numOfChildren = {}
        self.countNodes(root, numOfChildren)
        return self.quickSelectOnTree(root, k, numOfChildren)


    def countNodes(self, root, numOfChildren):
        if root is None:
            return 0

        left = self.countNodes(root.left, numOfChildren)
        right = self.countNodes(root.right, numOfChildren)
        numOfChildren[root] = left + right + 1
        return left + right + 1

    def quickSelectOnTree(self, root, k, numOfChildren):
        if root is None:
            return -1

        if root.left == None:
            left = 0
        else:
            left = numOfChildren[root.left]

        if left >= k:
            return self.quickSelectOnTree(root.left, k, numOfChildren)

        if left + 1 == k:
            return root.val

        return self.quickSelectOnTree(root.right, k - left - 1, numOfChildren)


from BinaryTree.BinaryTreeUtil import BinaryTree
data = "{20, 8, 22, 4, 12}"
root = BinaryTree().deserialize(data)
s = Solution()
print(s.kthLargest(root, 1))