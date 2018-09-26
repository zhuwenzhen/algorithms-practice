"""
398. Longest Increasing Continuous subsequence II
Give you an integer matrix (with row size n, column size m)，
find the longest increasing continuous subsequence in this matrix.
(The definition of the longest increasing continuous subsequence here
can start at any row or column and go up/down/right/left any direction).

Example
Given a matrix:

[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
return 25

Challenge
O(nm) time and memory.
"""

class Solution:
    """
    @param A: An integer matrix
    @return: an integer
    """

    def longestIncreasingContinuousSubsequenceII(self, A):
        if not A: return 0


        # initialization
        m, n = len(A), len(A[0])
        res = 0
        dp = [[0 for _ in range(n) ] for _ in range(m)]
        flag = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                dp[i][j] = self.search(i, j, A, dp, flag)
                res = max(res, dp[i][j])
        return res


    def search(self, x, y, A, dp, flag):
        if flag[x][y]: return dp[x][y] # pruning

        m, n = len(A), len(A[0])

        res = 1
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if A[x][y] > A[nx][ny]:
                    res = max(res, self.search(nx, ny, A, dp, flag) + 1)

        flag[x][y] = 1
        dp[x][y] = res
        return res