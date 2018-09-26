"""
427. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example
Given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helper(n, n, '', res)
        return res

    def helper(self, l, r, item, res):
        if l > r:
            return
        # exit recursion
        if l == 0 and r == 0:
            print('item! =', item)
            res.append(item)
        # first add left parenthesis n times
        if l > 0:
            print("l", item + '(')
            self.helper(l-1, r, item + '(', res)
        if r > 0:
            print("r", item + ')')
            self.helper(l, r-1, item + ')', res)

s = Solution()
s.generateParenthesis(3)