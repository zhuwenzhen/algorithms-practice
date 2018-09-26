"""
153. Combination Sum II
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Example
Given candidate set [10,1,6,7,2,1,5] and target 8,

A solution set is:

[
  [1,7],
  [1,2,5],
  [2,6],
  [1,1,6]
]
"""
import itertools
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target):
        res = []
        if candidates is None or target is None:
            return res

        candidates.sort()
        self.dfs([], candidates, 0, res, target)
        res.sort()
        print(res)
        res = list(res for res,_ in itertools.groupby(res))
        print(res)
        return res

    def dfs(self, combo, candidates, startIndex, res, target):
        if target == 0:
            res.append(combo.copy())
            return

        for i in range(startIndex, len(candidates)):
            if target < candidates[i]:
                break
            combo.append(candidates[i])
            self.dfs(combo, candidates, i+1, res, target - candidates[i])
            combo.pop()

# Better solution
class Solution2:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if candidates is None or target is None:
            return res

        candidates.sort()
        self.dfs([], candidates, 0, target, res)
        return res

    def dfs(self, combination, candidates, startIndex, target, res):
        if target == 0:
            res.append(combination.copy())
            return
        for i in range(startIndex, len(candidates)):

            if i != startIndex and candidates[i] == candidates[i - 1]:
                continue
            if target < candidates[i]:
                break
            combination.append(candidates[i])

            self.dfs(combination, candidates, i + 1, target - candidates[i], res)
            combination.pop()


candidates = [2,5,2,1,2]
target = 5

s2 = Solution2()
print(s2.combinationSum2(candidates, target))