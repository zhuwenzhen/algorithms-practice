"""
415. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Challenge
O(n) time without extra memory.
"""

"""
1. 在 i++ 和 j-- 的时候，要用 while 循环不断的跳过非英文字母
2. 比较的时候要都变成小写之后再比较
"""

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

    def isPalindrome2(self, s):
        s_list = [i.lower() for i in s if i.isalnum()]
        start, end = 0, len(s_list) - 1
        while start < end and start >= 0 and end <= len(s_list):
            print(s_list[start] , s_list[end])
            if s_list[start] != s_list[end]:
                return False
            start += 1
            end -= 1
        return True

s = Solution()
print(s.isPalindrome2("a.b,."))
