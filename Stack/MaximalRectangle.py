"""
510. Maximal Rectangle
Given a 2D boolean matrix filled with False and True,
find the largest rectangle containing all True and return its area.

Example
Given a matrix:

[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
return 6.
"""

class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        a = [0 for _ in range(n)]
        max_area = 0

        for i in range(m):
            for j in range(n):
                a[j] = a[j] + 1 if matrix[i][j] else 0
            max_area = max(max_area, self.longestRectangle(a))

        return  max_area

    def longestRectangle(self, height):
        stack = []
        i = 0
        area = 0

        while i < len(height):
            if not stack or height[i] > height[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[len(stack)-1]-1

                area = max(area, width * height[curr])
                i -= 1
            i += 1

        while stack:
            curr = stack.pop()
            if not stack: width = i
            else: width = len(height) - stack[len(stack) - 1] - 1
            area = max(area, width * height[curr])
        return area

s = Solution()
matrix = [
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]

print(s.maximalRectangle(matrix))






