



"""
在非二叉树上的深度优先搜索（Depth-first Search）中，
90%的问题，不是求组合（Combination）就是求排列（Permutation)

特别是组合类的深度优先搜索的问题特别的多。

本章节的先修内容有：

通过全子集问题 Subsets 了解组合类搜索的两种形式
通过全子集问题 II 了解如何在搜索中去重
"""

## [1, 2, 3] -> [], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]


class solution:
    def subsets(self, nums):
        res = []
        if nums is None:
            return res

        if not nums:
            return [[]]

        nums.sort()

        self.dfs([], nums, 0, res)
        return res

    def dfs(self, subset, nums, startIndex, res):

        res.append(subset.copy())

        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(subset, nums, i + 1, res)
            subset.pop()

