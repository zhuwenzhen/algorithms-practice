"""
76. Longest Increasing Subsequence
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

Example
For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4

Challenge
Time complexity O(n^2) or O(nlogn)
"""

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums: return 0
        n = len(nums)
        dp =[1 for _ in range(n)]

        for i, val in enumerate(nums):
            for j in range(i):
                if nums[j] < val:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)



s = Solution()
print(s.longestIncreasingSubsequence([5, 4, 1, 2, 3]))