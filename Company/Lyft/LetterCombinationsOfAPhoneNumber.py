"""
425. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        # write your code here
        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        res = []
        if not digits:
            return res
        self.dfs(digits, digitMap, 0, '', res)
        return res

    def dfs(self, digits, digitMap, index, curr, res):
        if index == len(digits):
            res.append(curr)
            return
        for i in range(len(digitMap[digits[index]])):
            self.dfs(digits, digitMap, index + 1, curr + digitMap[digits[index]][i], res)

input = '23'
s = Solution()
print(s.letterCombinations(input))