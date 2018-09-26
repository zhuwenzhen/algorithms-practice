
"""
425. Letter Combinations of a Phone Number
Given a digit string excluded 01, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Cellphone

Example
Given "23"

Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""

"""
Strong Hire: 两问的 DFS 都能写出来，第二问使用 Trie 或者 Hash 都可以，无需提示 
Hire / Weak Hire: 写完第一问的 DFS，第二问给出正确思路和方法，但是没写完，需要部分提示 
No Hire: 第一问没写完，或者 bug 很多 
Strong No: 没思路不会做


Letter Combinations of Phone Number 面试评分标准

"""

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    phonePadLetters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def letterCombinations(self, digits):
        if digits is None or len(digits) == 0:
            return []
        totalCount = 1
        for digit in digits:
            totalCount *= len(self.phonePadLetters[digit])

        answer = []

        for caseIndex in range(totalCount):
            currentCount = caseIndex
            currentString = ""
            for digit in digits:
                currentDigit = currentCount % len(self.phonePadLetters[digit])
                currentCount //= len(self.phonePadLetters[digit])
                currentString += self.phonePadLetters[digit][currentDigit]
            answer.append(currentString)

        return sorted(answer)


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

        results = []
        if not digits:
            return []

        self.dfs(digits, digitMap, 0, '', results)

        return results

    def dfs(self, digits, digitMap, index, currentSt, results):
        if index == len(digits):
            results.append(currentSt)
            return
        print("index", index)
        print(digits[index])

        for i in range(len(digitMap[digits[index]])):
            self.dfs(digits, digitMap, index + 1, currentSt + digitMap[digits[index]][i], results)


s = Solution()
s.letterCombinations('23')