"""
411. Gray Code
The gray code is a binary numeral system where
two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits
in the code, find the sequence of gray code.
A gray code sequence must begin with 0 and with cover all 2n integers.

Example
Given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

Challenge
O(2n) time.
"""

class Solution:
    # @param {int} n a number
    # @return {int[]} Gray code
    def grayCode(self, n):
        if n == 0:
            return [0]
        result = self.grayCode(n - 1)
        seq = list(result)
        for i in reversed(result):
            seq.append((1 << (n - 1)) | i)
        return seq