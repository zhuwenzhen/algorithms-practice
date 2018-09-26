"""
394. Coins in a Line
There are n coins in a line.
Two players take turns to take one or two coins from right side until there are no more coins left.
The player who take the last coin wins.
Could you please decide the first play will win or lose?

Example
n = 1, return true.
n = 2, return true.
n = 3, return false.
n = 4, return true.
n = 5, return true.

Challenge
O(n) time and O(1) memory
"""

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        dp = [0 for _ in range(n+1)]
        return self.memorySearch(n, dp)

    def memorySearch(self, n, dp):
        if dp[n] != 0:
            if dp[n] == 1:
                return False
            else:
                return True

        if n <= 0:
            dp[n] = 1
        elif n == 1:
            dp[n] = 2
        elif n == 2:
            dp[n] = 2
        elif n == 3:
            dp[n] = 1
        else:
            if (self.memorySearch(n-2, dp) and self.memorySearch(n-3, dp)) \
                or (self.memorySearch(n-3, dp) and self.memorySearch(n-4, dp)):
                dp[n] = 2
            else:
                dp[n] = 1
        if dp[n] == 2:
            return True

        return False

s = Solution()
print(s.firstWillWin(5))
