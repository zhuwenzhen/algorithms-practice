"""
1210. Increasing Subsequences
Given an integer array, your task is to find all
the different possible increasing subsequences of the given array,
and the length of an increasing subsequence should be at least 2 .

Example
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
"""

class Solution:
    """
    @param nums: an integer array
    @return: all the different possible increasing subsequences of the given array
    """
    def findSubsequences(self, nums):
        res = []

        if nums is None:
            return res
        if not nums:
            res.append([])
            return res

        nums.sort()
        candidate = []
        self.dfs(candidate, nums, 0, res)
        return res

    def dfs(self, candidate, nums, startIndex, res):
        if len(candidate) >= 2:
            res.append(tuple(candidate+[]))

        for i in range(startIndex, len(nums)):
            if i != startIndex and nums[i] == nums[i - 1]:
                    continue
            if candidate and nums[i] < candidate[-1]:
                continue
            candidate.append(nums[i])
            self.dfs(candidate, nums, i+1, res)
            candidate.pop()
        return


s = Solution()
arr = [4, 6, 7, 7]
print(s.findSubsequences(arr))