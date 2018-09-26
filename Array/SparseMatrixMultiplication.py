"""
654. Sparse Matrix Multiplication
Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        if A is None or B is None:
            return []
        if A[0] is None or B[0] is None:
            return []
        m = len(A)
        n = len(A[0])
        d = len(B[0])

        AB = [[0 for _ in range(d)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    for k in range(d):
                        AB[i][k] += A[i][j] * B[j][k]
        return AB

s = Solution()
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
print(s.multiply(A, B))

