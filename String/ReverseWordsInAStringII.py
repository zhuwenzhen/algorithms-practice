"""
927. Reverse Words in a String II
Given an input character array, reverse the array word by word.
A word is defined as a sequence of non-space characters.

The input character array does not contain leading or
trailing spaces and the words are always separated by a single space.

Example
Given s = "the sky is blue",
after reversing : "blue is sky the"

Challenge
Could you do it in-place without allocating extra space?
"""

class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, s):
        split = s.split(" ")
        return "".join(split)

    def reverseWords2(self, s):
        split = s.split(" ")
        left, right = 0, len(split) - 1
        while (left < right):
            split[left], split[right] = split[right], split[left]
            left += 1
            right -= 1
        return " ".join(split)



sol = Solution()
s = "the sky is blue"
print(sol.reverseWords2(s))

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Could you do it in-place without allocating extra space?
#

class Solution:
    def reverseWords(self, s):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(s, begin, end):
            for i in range((end - begin) // 2):
                s[begin + i], s[end - 1 - i] = s[end - 1 - i], s[begin + i]

        reverse(s, 0, len(s))
        i = 0
        for j in range(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j)
                i = j + 1

