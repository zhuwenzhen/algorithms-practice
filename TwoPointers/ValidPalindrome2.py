"""
891. Valid Palindrome II
Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Example
Given s = "aba" return true
Given s = "abca" return true // delete c
"""
"""
FLAG 的面经中出现过此题。
一个简单直观的粗暴想法是，既然要删除一个字母，
那么我们就 for 循环枚举（Enumerate）每个字母，
试试看删掉这个字母之后，该字符串是否为一个回文串。

上述粗暴算法的时间复杂度是 O(n^2)，
因为 for 循环枚举被删除字母的复杂度为 O(n)，
判断剩余字符构成的字符串是否为回文串的复杂度为 O(n)，
总共花费 O(n^2)

这显然一猜就应该不符合面试官的要求。
"""
class Solution:
    """
    @param s: a string
    @return: nothing
    """
    def validPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1

        if left >= right:
            return True

        deleteLeftCheck = self.validSubPalindrome(s, left + 1, right)
        deleteRightCheck = self.validSubPalindrome(s, left, right - 1)
        return deleteLeftCheck or deleteRightCheck

    def validSubPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True