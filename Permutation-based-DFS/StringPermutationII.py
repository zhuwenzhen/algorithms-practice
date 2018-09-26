"""
10. String Permutation II
Given a string, find all permutations of it without duplicates.

Example
Given "abb", return ["abb", "bab", "bba"].

Given "aabb", return ["aabb", "abab", "baba", "bbaa", "abba", "baab"].
"""

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        self.res = []
        if str is None:
            return [""]
        nums = sorted([i for i in str])
        print(nums)
        self.dfs_str2("", nums)
        return self.res

    def dfs_str2(self, candidate, nums):
        if nums == []:
            self.res.append(candidate)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            self.dfs_str2(candidate + nums[i], nums[:i] + nums[i+1:])