"""
397. Longest Continuous Increasing Subsequence
Give an integer array，find the longest increasing continuous subsequence in this array.

An increasing continuous subsequence:

Can be from right to left or from left to right.
Indices of the integers in the subsequence should be continuous.
Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.
"""

class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        if not A or A is None: return 0

        # initialization
        longest = 1
        memo = [0 for _ in range(len(A))]
        memo[0] = 1

        for i in range(1, len(A)):
            if A[i - 1] > A[i]: # decreasing
                memo[i] = memo[i - 1] + 1
            else:
                memo[i] = 1
            longest = max(longest, memo[i])

        for i in range(1, len(A)):
            if A[i - 1] < A[i]: # increasing
                memo[i] = memo[i - 1] + 1
            else:
                memo[i] = 1
            longest = max(longest, memo[i])

        return longest
