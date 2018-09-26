"""
680. Split String
Give a string, you can choose to split the string after one character
or two adjacent characters,
and make the string to be composed of only one character or two characters.
Output all possible results.

Example
Given the string "123"
return [["1","2","3"],["12","3"],["1","23"]]
"""


class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        self.res, candidate = [], []
        self.s = s
        if s is None: return self.res
        self.dfs(candidate, 0)
        return self.res

    def dfs(self, candidate, index):
        if index == len(self.s):
            self.res.append(candidate)
            return
        i = index
        while i < min(index + 2, len(self.s)):
            self.dfs(candidate + [self.s[index: i + 1]], i + 1)
            i += 1