"""
390. Find Peak Element II
There is an integer matrix which has the following features:

The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:

A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
Find a peak element in this matrix. Return the index of the peak.

Example
Given a matrix:

[
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

Challenge
Solve it in O(n+m) time.

If you come up with an algorithm that you thought it is O(n log m) or O(m log n),
can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?
"""

class Solution:
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        if not A or A is None: return []

        if A[0] is None or not A[0]: return []

        m = len(A)
        n = len(A[0])
        return self.find(1, m - 2, 1, n - 2, A)


    def find(self, x1, x2, y1, y2, A):
        midX = x1 + (x2 - x1) // 2
        midY = y1 + (y2 - y1) // 2

        x = midX
        y = midY

        max = A[x][y]
        for i in range(y1, y2 + 1):
            if A[x][i] > max:
                max = A[x][i]
                x = midX
                y = i

        for i in range(x1, x2 + 1):
            if A[i][midY] > max:
                max = A[i][midY]
                x = i
                y = midY

        isPeak = True

        if A[x - 1][y] > A[x][y]:
            isPeak = False
            x -= 1
        elif A[x + 1][y] > A[x][y]:
            isPeak = False
            x += 1
        elif A[x][y-1] > A[x][y]:
            isPeak = False
            y -= 1
        elif A[x][y+1] > A[x][y]:
            isPeak = False
            y += 1

        if isPeak:
            return [x, y]

        if x >= x1 and x < midX and y >= y1 and y < midY:
            return self.find(x1, midX - 1, y1, midY - 1, A)

        if x >= 1 and x < midX and y > midY and y <= y2:
            return self.find(x1, midX - 1, midY - 1, y2, A)

        if x > midX and x <= x2 and y >= y1 and y < midY:
            return self.find(midX + 1, x2, midY + 1, y2, A)

        if x >= midX and x <= x2 and y > midY and y <= y2:
            return self.find(midX + 1, x2, midY + 1, y2, A)

        return [-1, -1]

matrix = [
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]

s = Solution()

print(s.findPeakII(matrix))