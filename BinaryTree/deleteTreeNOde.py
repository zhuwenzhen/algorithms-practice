"""
给一个删除树节点的函数，和root，怎么遍历删除整棵树。用了postorder recursion。. 一亩-三分-地，独家发布
问这个程序可能会crash，为什么。  因为recursion太多可能会memory overflow。
问怎么避免，用level order，空间复杂度O(n).

如果还是太大，怎么办，我就不会了，他提示说serialize，我想到了线索化二叉树，但是太难了，不会，postorder iteration也太难了，不会。.1point3acres网
这些复习的时候都看到过，觉得肯定不会考，所以也怨不得别人。
"""

# https://leetcode.com/problems/delete-node-in-a-bst/


def deleteTree(root):
    while root:
        next_root = root.left
        if not next_root:
            next_root = root.right
            deleteNode(root)
        else:
            predecessor = root.left
            while predecessor.right: predecessor = predecessor.right
            predecessor.right = root
    root = next_root

def deleteNode(self, root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    if root is None: return
    if root.val == key:
        if root.right and root.left:
            right = root.right
            while right is not None and right.left is not None: right = right.left
            right.left = root.left
            return root.right
        else:
            if root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None

    elif key > root.val:
        root.right = self.deleteNode(root.right, key)
    else:
        root.left = self.deleteNode(root.left, key)

    return root