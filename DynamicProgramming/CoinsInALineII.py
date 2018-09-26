"""
395. Coins in a Line II
There are n coins with different value in a line.
Two players take turns to take one or two coins from left side until there are no more coins left.
The player who take the coins with the most value wins.

Could you please decide the first player will win or lose?

Example
Given values array A = [1,2,2], return true.

Given A = [1,2,4], return false.
"""

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, coins):
        n = len(coins)
        if n == 1: return True
        sum = [0 for _ in range(n + 1)] # last i coins' sum
        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            sum[i] = sum[i-1] + coins[n-i]

        dp[0] = 0
        dp[1] = coins[n-1]
        dp[2] = coins[n-2]+coins[n-1]

        for i in range(2, n+1):
            dp[i] = max(sum[i] - dp[i-1], sum[i] - dp[i-2])

        return dp[n] > sum[n] // 2
