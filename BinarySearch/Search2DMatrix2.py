"""
38. Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix,
return the occurrence of it.

This matrix has the following properties:
    Integers in each row are sorted from left to right.
    Integers in each column are sorted from up to bottom.
    No duplicate integers in each row or column.

Example
Consider the following matrix:

[
  [1, 3, 5, 7],
  [2, 4, 7, 8],
  [3, 5, 9, 10]
]
Given target = 3, return 2.

Challenge
O(m+n) time and O(1) extra space
"""


"""
+ 复杂度要求 —— O(m+n) time and O(1) extra space，
    + 同时输入只满足自顶向下和自左向右的升序，行与行之间不再有递增关系，
    + 与上题有较大区别。时间复杂度为线性要求，
    + 因此可从元素排列特点出发，
    + 从一端走向另一端无论如何都需要m+n步，因此可分析对角线元素。
+ 首先分析如果从左上角开始搜索，
    + 由于元素升序为自左向右和自上而下，
    + 因此如果target大于当前搜索元素时还有两个方向需要搜索，不太合适。
+ 如果从右上角开始搜索，
    + 由于左边的元素一定不大于当前元素，
    + 而下面的元素一定不小于当前元素，
    + 因此每次比较时均可排除一列或者一行元素
    +（大于当前元素则排除当前行，小于当前元素则排除当前列，由矩阵特点可知），可达到题目要求的复杂度。
"""

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # 首先对输入做异常处理，
        # 不仅要考虑到matrix为空串，还要考虑到matrix[0]也为空串。
        if not matrix or not matrix[0]:
            return 0
        occur = 0
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        # 注意循环终止条件
        while row < m and col >= 0:
            if matrix[row][col] == target:
                occur += 1
                col -= 1 # 在找出target后应继续向左搜索其他可能相等的元素，
                # #下方比当前元素大，故排除此列。
            elif matrix[row][col] < target: # < target, go down (larger) keep searching
                row += 1
            else: # > target, go left (smaller side)
                col -= 1
        return occur


"""
源码分析
首先对输入做异常处理，不仅要考虑到matrix为空串，还要考虑到matrix[0]也为空串。
注意循环终止条件。

在找出target后应继续向左搜索其他可能相等的元素，下方比当前元素大，故排除此列。
严格来讲每次取二维矩阵元素前都应该进行 null 检测。

复杂度分析
由于每行每列遍历一次，故时间复杂度为 O(m + n)O(m+n).
"""