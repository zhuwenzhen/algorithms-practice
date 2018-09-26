"""
392. House Robber
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them
is that adjacent houses have security system connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Example
Given [3, 8, 4], return 8.

Challenge
O(n) time and O(1) memory.
"""

class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if not A or A is None: return 0
        n  = len(A)

        # state
        dp = [0 for _ in range(n + 1)] # dp[i]: in the first i houses, max value you can steal

        # initialization
        dp[0] = 0
        dp[1] = A[0]

        # function
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + A[i-1])

        return dp[n]