"""
1444. Dyeing Problem
There is a circle, divided into n sectors. All the sectors are colored with some of m colors. The colors of adjacent sectors cannot be the same. Find the total number of plans.

Example
Given n = 2, m = 3, return 6.

Explanation:
One circle is divided into two sectors. There are six kinds of schemes for coloring in three colors: black, red, black and white, white and red, white and black, red and white, and red and black.
Given n = 3, m = 2, return 0.

Explanation:
A circle is divided into 3 sectors and colored with 2 colors. No matter how it is colored, there is no guarantee that the adjacent colors are different.
"""

class Solution:
    """
    @param n: the number of sectors
    @param m: the number of colors
    @return: The total number of plans.
    """
    def getCount(self, n, x):
        return (x - 1)**n + (-1)**n *(x-1)

s = Solution()

print(s.getCount(1000, 1800))
