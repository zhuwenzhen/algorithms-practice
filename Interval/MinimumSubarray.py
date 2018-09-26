"""
44. Minimum Subarray
Given an array of integers, find the subarray with smallest sum.
Return the sum of the subarray.

Example
For [1, -1, -2, 1], return -3.
"""
class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    def minSubArray(self, nums):
        if nums is None and not nums:
            return 0

        maxSum = 0
        sum, minSum = 0, nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum - maxSum < minSum:
                minSum = sum - maxSum
            if sum > maxSum:
                maxSum = sum
        return minSum