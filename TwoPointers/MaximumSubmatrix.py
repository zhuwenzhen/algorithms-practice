"""
944. Maximum Submatrix
Given an n x n matrix of positive and negative integers,
find the submatrix with the largest possible sum.

Example
Given matrix =
[
[1,3,-1],
[2,3,-2],
[-1,-2,-3]
]

return 9.

Explanation:
the submatrix with the largest possible sum is:
[
[1,2],
[2,3]
]
"""
import sys

class Solution:
    def maxSubmatrix_TwoPointers(self, arr):
        if arr is None or not arr:
            return 0

        l, r = 0, 0
        currSum, maxSum, = 0, 0
        maxUp, maxDown, maxLeft, maxRight = 0, 0, 0, 0
        m = len(arr)
        n = len(arr[0])
        for i in range(m):
            for j in range(n):

                currSum = self.getSubarraySum(arr[:][j])









    def maxSubmatrix_DP(self, arr):
        r, c = len(arr), len(arr[0])
        dp = [[0 for _ in range(c)] for _ in range(c)]
        maximum, init = 0, False
        for i in range(r):
            for j in range(c):
                sum = 0
                print(init, maximum)
                for k in range(j, -1, -1):
                    # print('i','j','k')
                    # print(i, j, k, arr[i][k])
                    sum += arr[i][k]
                    tmp = dp[k][j] + sum
                    dp[k][j] = max(0, tmp)
                    if not init or tmp > maximum:
                        init = True
                        maximum = tmp
                # print(dp)
        return maximum

    def maxSubmatrix(self, matrix):
        if matrix is None or not matrix:
            return 0
        if not matrix[0]:
            return 0

        n = len(matrix)
        maximum = -10e5

        for i in range(n):
            for j in range(i, n):
                arr = self.compression(matrix, i, j)
                sum = self.getSubarraySum(arr)
                maximum = max(maximum, sum)
        return maximum

    def compression(self, matrix, i, j):
        n = len(matrix)
        arr = [0 for _ in range(n)]
        for index in range(n):
            for k in range(i, j + 1):
                arr[index] += matrix[k][index]
        return arr

    def getSubarraySum(self, arr):
        sum, minSum = 0, 0
        maximum = -10e5
        n = len(arr)

        for i in range(n):
            sum += arr[i]
            maximum = max(maximum, sum - minSum)
            minSum = min(sum, minSum)
        return maximum

matrix = [
    [1, 3, -1],
    [2, 3, -2],
    [-1, -2, -3]
]

s = Solution()
print(s.maxSubmatrix(matrix))
