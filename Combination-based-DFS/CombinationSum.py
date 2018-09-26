"""
135. Combination Sum
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Example
Given candidate set [2,3,6,7] and target 7, a solution set is:

[7]
[2, 2, 3]
"""

"""
• Combination Sum 限制了组合中的数之和
    •  加入一个新的参数来限制 
• Subsets 无重复元素，Combination Sum 有重复元素
    • 需要先去重 
• Subsets 一个数只能选一次，Combination Sum 一个数可以选很多次
    • 搜索时从 index 开始而不是从 index + 1
"""

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    #
    # def combinationSum(self, candidates, target):
    #     res = []
    #     if candidates is None or target is None:
    #         return res
    #
    #     candidates.sort()
    #     self.dfs([], candidates, 0, res, target)
    #     return res
    #
    # def dfs(self, combo, candidates, startIndex, res, target):
    #     # 3. end of recursion:
    #     if target == 0:
    #         res.append(combo.copy())
    #         return
    #
    #     # step 2: break recursion into sub-prob:
    #     for i in range(startIndex, len(candidates)):
    #         if target < candidates[i]:
    #             break
    #         combo.append(candidates[i])
    #         self.dfs(combo, candidates, i, res, target - candidates[i])
    #         combo.remove(combo[-1])

    def combinationalSum(self, candidates, target):
        res = []
        if candidates is None or not candidates or target is None:
            return res

        candidates.sort()

        # run dfs / backtracking on it
        self.dfs()

    def dfs(self, candidates, target, combo, startIndex, res):
        # end of recursion
        if target == 0:
            res.append(combo.copy())
            return

        # break into sub prob
        for i in range(startIndex, len(candidates)):
            if target < candidates[i]:
                break
            combo.append(candidates[i])
            new_target = target - candidates[i]
            self.dfs(candidates, new_target, combo, i, res)
            combo.pop() # back track to prev state