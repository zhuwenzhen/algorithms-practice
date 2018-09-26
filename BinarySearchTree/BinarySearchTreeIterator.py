"""
86. Binary Search Tree Iterator
Design an iterator over a binary search tree with the following rules:

Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
Example
For the following binary search tree,
in-order traversal by using iterator is [1, 6, 10, 11, 12]

   10
 /    \
1      11
 \       \
  6       12
Challenge
Extra memory usage O(h), h is the height of the tree.

Super Star: Extra memory usage O(1)
"""

"""
Definition of TreeNode:


Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class BSTIterator:
    # @param root: The root of binary tree.
    def __init__(self, root):
        self.stack = []
        self.curr = root

    # @return: True if there has next node, or false
    def hasNext(self):
        return self.curr is not None or len(self.stack) > 0

    # @return: return next node
    def next(self):
        while self.curr is not None:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        next = self.curr
        self.curr = self.curr.right
        return next

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.curr = root

    # check if BST has next node, True if there is
    def hasNext(self):
        return self.curr is None or self.stack

    # return next node
    def next(self):
        while self.curr is not None:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        next = self.curr
        self.curr = self.curr.right

        return next