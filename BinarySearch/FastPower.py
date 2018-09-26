"""
140. Fast Power
Calculate the an % b where a, b and n are all 32bit integers.

Example
For 231 % 3 = 2
For 1001000 % 1000 = 0
Challenge
O(logn)
"""

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    # 非递归版本，思路是转换为二进制
    # 注意幂次是二进制：
    # a^(1010)2  = a^(1000)2 * a^(10)2
    def fastPower(self, a, b, n):
        res = 1
        while n > 0:
            if n % 2 == 1:
                res = res * a % b
            a = a * a % b
            n = n // 2
        return res % b

    # recursion
    def fastPower(self, a, b, n):
        if n == 1:
            return a % b
        if n == 0:
            return 1 % b

        prod = self.fastPower(a, b, n // 2)
        prod = prod * prod % b
        if n % 2 == 1:
            prod = (prod * (a % b)) % b
        return prod
