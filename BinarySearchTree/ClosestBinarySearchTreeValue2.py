"""
901. Closest Binary Search Tree Value II
Given a non-empty binary search tree and a target value,
find k values in the BST that are closest to the target.

Example
Given root = {1}, target = 0.000000, k = 1, return [1].

Challenge
Assume that the BST is balanced,
could you solve it in less than O(n) runtime
(where n = total nodes)?
"""

"""
Strong Hire 找1个点和找k个点都答出来，且找 k 个点的能用 O(k + logn) 的时间复杂度 
Hire 找1个点和找k个点都答出来，且找 k 个点的能用 O(klogn) 的时间复杂度完成，少 bug，无需提示 
Weak Hire: 找1个点和找k个点都答出来，且找 k 个点的能分别用 O(klogn) 和 O(n) 的时间复杂度完成，bug 多，需
要提示 
No Hire 答出1个点，答不出 k 个点非O(n)的算法 
Strong No Hire 啥都答不出来

"""
#  https://www.jiuzhang.com/solution/closest-binary-search-tree-value-ii/
"""
耍流氓法， 先来一个inorder 再把find k 个接近点的方法照抄一遍。 事实证明，题还是需要背的
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        # write your code here
        if root is None or k == 0:
            return []
        self.list = []
        self.inOrder(root)
        print(self.list)
        res = self.findKth(self.list, target, k)

        return res

    def findKth(self, list, target, k):
        start, end = 0, len(list) - 1

        while start + 1 < end:
            mid = (start + end) / 2
            if list[mid] < target:
                start = mid
            else:
                end = mid
        out = []
        while len(out) < k:
            leftDiff = abs(target - list[start]) if start >= 0 else None
            rightDiff = abs(target - list[end]) if end < len(list) else None

            if rightDiff != None and leftDiff != None:
                if rightDiff < leftDiff:
                    out.append(list[end])
                    end += 1
                else:
                    out.append(list[start])
                    start -= 1
            elif leftDiff != None:
                out.append(list[start])
                start -= 1
            elif rightDiff != None:
                out.append(list[end])
                end += 1

        return out

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        self.list.append(root.val)
        self.inOrder(root.right)