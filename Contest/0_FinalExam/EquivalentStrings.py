"""
1376. Equivalent Strings
Given you two strings with same length, return true if they are equivalent.

Two strings a and b of equal length are called equivalent in one of the two cases:

They are equal.
If we split string a into two halves of the same size a1 and a2, and string b into two halves of the same size b1 and b2, then one of the following is correct:
a1 is equivalent to b1, and a2 is equivalent to b2
a1 is equivalent to b2, and a2 is equivalent to b1
Example
Example 1:

Input: s1 = "aaba", s2 = "abaa"
Output: true
Example 2:

Input: s1 = "aabb", s2 = "abab"
Output: false
"""

class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: is s1 and s2 are equivalent
    """
    def isEquivalentStrings(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        if n1 != n2: return False

        if s1 == s2:
            return True

        half_len = n1 // 2

        if n1 % 2 == 1:
            return s1 == s2
        else:
            a1 = s1[:half_len]
            a2 = s1[half_len:]
            b1 = s2[:half_len]
            b2 = s2[half_len:]
            if self.isEquivalentStrings(a1, b1) \
                and self.isEquivalentStrings(a2, b2) \
                or self.isEquivalentStrings(a1, b2) \
                and self.isEquivalentStrings(a2, b1):
                return True
            return False

s1 = "hagnzomowtledfdotnll"
s2 = "ledfdotnllomowthagnz"
s = Solution()
print(s.isEquivalentStrings(s1, s2))