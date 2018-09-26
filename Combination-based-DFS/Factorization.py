"""
652. Factorization
A non-negative numbers can be regarded as product of its factors.
Write a function that takes an integer n and return all possible combinations of its factors.

Example
Given n = 8
return [[2,2,2],[2,4]]
// 8 = 2 x 2 x 2 = 2 x 4.

Given n = 1
return []

Given n = 12
return [[2,6],[2,2,3],[3,4]]
"""
import math

class Solution:

    def getFactors(self, n):
        res = []
        self.dfs(2, n, [], res)
        return res


    def dfs(self, start, n, factors, res):
        # exit of recursion
        if n <= 1:
            if len(factors) > 1:
                res.append(factors.copy())
            return

        end = math.floor(math.sqrt(n))

        for i in range(start, end + 1):
            if n % i == 0: # means i is a factor
                factors.append(i)
                self.dfs(i, n // i, factors, res)
                factors.pop() # backtrack to prev states

        if n >= start:
            factors.append(n)
            self.dfs(n, 1, factors, res) # I don't understand why n = 1 here
            factors.pop()

n = 8
s = Solution()
print(s.getFactors(n))
