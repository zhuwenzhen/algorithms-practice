"""
33. N-Queens
The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example
There exist two distinct solutions to the 4-queens puzzle:
[
  // Solution 1
  [".Q..",
   "...Q",
   "Q...",
   "..Q."
  ],
  // Solution 2
  ["..Q.",
   "Q...",
   "...Q",
   ".Q.."
  ]
]
Challenge
Can you do it without recursion?
"""


class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens.
    @return: All distinct solutions.
    """
    n = 0
    results = []
    cols = {}

    def attack(self, row, col):
        for c, r in self.cols.iteritems():
            if c - r == col - row or c + r == col + row:
                return True
        return False

    def search(self, row):
        if row == self.n:
            result = []
            for i in range(self.n):
                r = ['.'] * self.n
                r[self.cols[i]] = 'Q'
                result.append(''.join(r))
            self.results.append(result)
            return

        for col in range(self.n):
            if col in self.cols:
                continue
            if self.attack(row, col):
                continue
            self.cols[col] = row
            self.search(row + 1)
            del self.cols[col]

    def solveNQueens(self, n):
        self.n = n
        self.search(0)
        return self.results
