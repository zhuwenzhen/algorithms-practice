"""
1458. Minimum Submatrix
Given a matrix arr of size n*m,
each position of the matrix has a positive or negative integer,
requiring a non-empty submatrix to be taken from the matrix
to minimize the sum of it,output the sum of the minimum submatrix.

Example
Given a = [[-3,-2,-1],[-2,3,-2],[-1,3,-1]]，return -7.

 Explanation:
The upper-left corner of the submatrix is (0,0),
and the lowerright corner is (1,2). The minimum sum is -7.
Given a = [[1,1,1],[1,1,1],[1,1,1]], return 1

Explanation:
All numbers are positive,
but the submatrix cannot be empty, so we take the smallest one.

"""

class Solution:

    def minimumSubmatrix(self, arr):
        r, c = len(arr), len(arr[0])
        dp = [[0 for _ in range(c)] for _ in range(c)]
        mn, init = 0, False
        for i in range(r):
            for j in range(c):
                sum = 0
                for k in range(j, -1, -1):
                    sum += arr[i][k]
                    tmp = dp[k][j] + sum
                    dp[k][j] = min(0, tmp)
                    if not init or tmp < mn:
                        init = True
                        mn = tmp
        return mn