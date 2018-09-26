"""
49. Sort Letters by Case
Given a string which contains only letters.
Sort it by lower case first and upper case second.

Example
For "abAcD", a reasonable answer is "acbAD"

Challenge
Do it in one-pass and in-place.
"""
class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        l, r = 0, len(chars) - 1
        while l < r:
            while l < r and not chars[l].isupper():
                l += 1
            while l < r and chars[r].isupper():
                r -= 1
            if l < r:
                chars[l], chars[r] = chars[r], chars[l]

        return chars