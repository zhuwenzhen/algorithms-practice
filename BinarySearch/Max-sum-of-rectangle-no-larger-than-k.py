

from bisect import *
class Solution:
    """
    @param matrix: a 2D matrix
    @param k: an integer
    @return: the max sum of a rectangle in the matrix such that its sum is no larger than k
    """
    def maxSumSubmatrix(self, matrix, k):
        # Write your code here
        row = len(matrix)
        col = len(matrix[0])

        preSum = [[0] for i in range(row)]
        for i in range(row):
            for j in range(col):
                preSum[i].append(preSum[i][-1] + matrix[i][j])

        ans = float('-inf')
        for j1 in range(col):
            for j2 in range(j1, col):
                tmpSum = []
                size = 0
                tmp = 0
                for i in range(row):
                    tmp += preSum[i][j2 + 1] - preSum[i][j1]
                    if tmp <= k and tmp > ans:
                        ans = tmp
                    if i == 0:
                        tmpSum.append(tmp)
                        size += 1
                        continue
                    else:
                        idx = bisect_left(tmpSum, tmp - k)
                        if idx < size and tmp - tmpSum[idx] > ans:
                            ans = tmp - tmpSum[idx]
                        insort_left(tmpSum, tmp)
                        size += 1

        return ans