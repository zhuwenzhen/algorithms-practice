"""
1375. Substring With At Least K Distinct Characters
There is a string S.S only contain lower case English character.
return the number of substrings there are that contain at least k distinct characters.

Example
Example 1:

Input: S = "abcabcabca", k = 4
Output: 0
Example 2:

Input: S = "abcabcabcabc", k = 3
Output: 55
"""
import collections
class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        dp = collections.defaultdict(int)
        n = len(s)
        distance = 0
        res = 0
        l = 0
        for i, c in enumerate(s):
            #print(i, c)
            dp[c] += 1
            if dp[c] == 1:
                distance += 1
                #print("dist", distance)
            while distance == k:
                res += n - i
                #print("num of substr", res)
                dp[s[l]] -= 1
                if dp[s[l]] == 0:
                    # print(dp[s[l]], s[l], l)
                    distance -= 1
                l += 1
        return res



sol = Solution()
s = "abcabcabcabc"
k = 4

sol.kDistinctCharacters(s, 3)