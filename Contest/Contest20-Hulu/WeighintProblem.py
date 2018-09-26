"""
1417. Weighing Problem
Gives n coins, each weighing 10g,
but the weight of one coin is 11g.
There is now a balance that can be accurately weighed.
Ask at least a few times to be sure to find the 11g gold coin.

Example

Given n = 3, return 1.

Explanation:
Select two gold coins on the two ends of the balance.
If the two ends of the balance are level,
the third gold coin is 11g, otherwise the heavy one is 11g.

Given n = 4, return 2.

Explanation:
Four gold coins can be divided into two groups
and placed on both ends of the scale.
According to the weighing results,
select the two heavy gold coins and place them
on the two ends of the balance for the second weighing.
The gold coin at the heavy end is 11g gold coins.
"""

class Solution:
    """
    @param n: The number of coins
    @return: The Minimum weighing times int worst case
    """
    # def minimumtimes(self, n):
    #     import math
    #     res = 0
    #     while n > 1:
    #         n = math.ceil( n /3.)
    #         res += 1
    #     return res

    def minimumtimes(self, n):
        import math
        res = 0
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return 1
        if n % 3 == 0:
            res = int(math.ceil(math.log(n, 3)))
        elif n % 3 == 1:
            res = int(math.ceil(math.log(n - 1, 3)))
        else:
            res = int(math.ceil(math.log(n - 2, 3)))
        return res


test = range(111)
s = Solution()
for t in test:
    print(t, " ",s.minimumtimes(t))
