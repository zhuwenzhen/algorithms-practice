"""
138. Subarray Sum
Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the last number.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of
    the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # sumOfSubarray[i, j] = prefixSum[j+1] - prefixSum[i]= 0
        # prefixSum[j+1] = prefixSum[i]
        hash = {}
        hash[0] = -1
        prefixSum = 0
        res = []
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum in hash:
                res.append(hash[prefixSum] + 1)
                res.append(i)
                return res

            hash[prefixSum] = i

        return res


