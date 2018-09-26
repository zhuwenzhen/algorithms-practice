"""

41. Maximum Subarray
Given an array of integers, find a contiguous subarray which has the largest sum.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Challenge
Can you do it in time complexity O(n)?
"""

"""
采用滑动窗口解决。sum 如果小于0，置为0，再加上当前值。
然后再与max相比，取大的。 1分钟AC
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        max_sum = -1e10
        sum = 0
        n = len(nums)

        for i in range(n):
            if sum < 0: sum = 0
            sum += nums[i]
            max_sum = max(max_sum, sum)
        return max_sum
