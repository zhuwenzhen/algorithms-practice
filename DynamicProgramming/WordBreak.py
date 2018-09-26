"""
107. Word Break
Given a string s and a dictionary of words dict,
determine if s can be break into a space-separated sequence of one or more dictionary words.

Example
Given s = "lintcode", dict = ["lint", "code"].
Return true because "lintcode" can be break as "lint code".
"""

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    cache = {}
    def wordBreak(self, s, dict):
        if not s:
            return True
        return self.dp(s, 0, 1, dict)

    def dp(self, s, prefix_start, suffix_start, dict):
        if (prefix_start, suffix_start) in self.cache:
            return self.cache[(prefix_start, suffix_start)]

        prefix = s[prefix_start:suffix_start]
        suffix = s[suffix_start:]

        # corner case / base case
        if not prefix and not suffix:
            return True
        # prefix in dict and solve
        flag1 = False
        if prefix in dict and self.dp(s, suffix_start, suffix_start, dict):
            flag1 = True
        flag2 = False
        if len(suffix) > 0 and self.dp(s, prefix_start, suffix_start + 1, dict):
            flag2 = True

        res = flag1 or flag2
        self.cache[(prefix, suffix)] = res
        return res


s = Solution()
print(s.wordBreak('lintcode', ['li', 'nt', 'code']))