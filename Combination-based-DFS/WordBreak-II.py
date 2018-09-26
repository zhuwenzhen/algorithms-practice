"""
582. Word Break II
Given a string s and a dictionary of words dict,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Example
Gieve s = lintcode,
dict = ["de", "ding", "co", "code", "lint"].

A solution is ["lint code", "lint co de"].
"""
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        res = []
        if s is None or wordDict is None:
            return res
        self.dfs_word_break(s, wordDict, [], 0, res)
        return res

    def dfs_word_break(self, s, wordDict, subset, startIndex, res):
        if ''.join(subset) == s:
            res.append(" ".join(subset.copy()))
            return
        if ''.join(list(reversed(subset))) == s:
            res.append(" ".join(list(reversed(subset))))
            return

        for i in range(startIndex, len(wordDict)):
            subset.append(list(wordDict)[i])
            self.dfs_word_break(s, wordDict, subset, i + 1, res)
            subset.pop()
