"""
407. Plus One
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.

Example
Given [1,2,3] which represents 123, return [1,2,4].
Given [9,9,9] which represents 999, return [1,0,0,0].
"""
class Solution:
    def plusOne(self, digits):
        strnum = ''
        for i in digits:
            strnum += str(i)
        res = []
        num = int(strnum) + 1
        while num:
            res.append(num % 10)
            num //= 10
        res.reverse()
        return res