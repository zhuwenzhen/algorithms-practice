"""
436. Maximal Square
Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing all 1's and return its area.

Example
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.
"""

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        if not matrix or matrix is None: return 0
        m, n = len(matrix), len(matrix[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1, m):
            dp[i][0] = matrix[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    # check up, left upper, left
                    dp[i][j] = 1 + min(dp[i-1][j], min(dp[i-1][j-1], dp[i][j-1]))
        a = 0
        for i in range(m):
            for j in range(n):
                a = max(a, dp[i][j])

        area = a ** 2
        return area



s = Solution()
matrix = [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
print(s.maxSquare(matrix))