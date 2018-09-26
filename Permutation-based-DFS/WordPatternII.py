"""
829. Word Pattern II
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern
and a non-empty substring in str.(i.e if a corresponds to s,
then b cannot correspond to s.

For example, given pattern = "ab", str = "ss", return false.)

Example
Given pattern = "abab", str = "redblueredblue", return true.
Given pattern = "aaaa", str = "asdasdasdasd", return true.
Given pattern = "aabb", str = "xyzabcxzyabc", return false.
"""

"""
Time Complexity: O(N)
Space Complexity: O(N)
"""

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """

    res = False
    def wordPatternMatch(self, pattern, str):
        map = {}


    def helper(self, pattern, str, map):
        map = {}
        p_len = len(pattern)
        s_len = len(str)

        if p_len == 0 and s_len == 0:
            return True

        if p_len == 0 or s_len == 0:
            return False

        if pattern[0] in map.keys():
            prefix = map.get(pattern[0])
            if str.startswith(prefix):
                return False
            return self.helper(pattern[1], str[:len(prefix)], map)


pattern = "abab"
string = "redblueredblue"

s = Solution()
print(s.wordPatternMatch(pattern, string))