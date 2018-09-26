"""
414. Divide Two Integers
Divide two integers without using multiplication,
division and mod operator.

If it is overflow, return 2147483647

Example
Given dividend = 100 and divisor = 9, return 11.
"""

class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        INT_MAX = 2147483647
        if divisor == 0:
            if dividend >= 0: return INT_MAX
            else: return -INT_MAX

        if dividend == 0:
            return 0

        if dividend == - INT_MAX and divisor == -1:
            return INT_MAX

        isNegative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)

        a = abs(dividend)
        b = abs(divisor)

        res = 0

        while a >= b:
            shift = 0
            while a >= (b << shift):
                shift += 1

            a -= b << (shift - 1)
            res += 1 << (shift - 1)

        if isNegative: return -res
        else: return res