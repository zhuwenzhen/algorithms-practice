"""
428. Pow(x, n)
Implement pow(x, n).

Example
Pow(2.1, 3) = 9.261
Pow(0, 1) = 0
Pow(1, 0) = 1

Challenge
O(logn) time
"""
class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = abs(n)
        if n == 0:
            return 1
        if n % 2 == 0:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp

        else:
            tmp = self.myPow(x, n // 2)
            return tmp * tmp * x