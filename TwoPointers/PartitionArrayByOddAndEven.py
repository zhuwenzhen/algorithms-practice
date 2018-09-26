"""
373. Partition Array by Odd and Even
Partition an integers array into odd number first and even number second.

Example
Given [1, 2, 3, 4], return [1, 3, 2, 4]

Challenge
Do it in-place.
"""

class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        start, end = 0, len(nums)-1
        while start < end:
            while start < end and nums[start] % 2 == 1: start += 1
            while start < end and nums[end] % 2 == 0: end -=1
            if start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1