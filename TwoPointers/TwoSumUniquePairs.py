"""
587. Two Sum - Unique pairs
Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

Example
Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        if nums is None or len(nums) < 2:
            return 0

        start = 0
        end = len(nums) - 1
        nums.sort()

        count = 0
        while start < end:
            if nums[start] + nums[end] == target:
                count += 1
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return count
