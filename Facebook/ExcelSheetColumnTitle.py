"""
1350. Excel Sheet Column Title
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

Example
1 -> A
2 -> B
3 -> C
 ...
26 -> Z
27 -> AA
28 -> AB
"""

class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        sheet = {}
        for i in range(26):
            sheet[i] = alphabets[i]

        res = ''
        while n > 0:
            res = sheet[(n - 1) % 26] + res
            n = (n - 1) // 26
        return res

s = Solution()

print(s.convertToTitle(53))