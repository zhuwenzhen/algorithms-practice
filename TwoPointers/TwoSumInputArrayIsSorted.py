"""
608. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target,
where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

Example
Given nums = [2, 7, 11, 15], target = 9
return [1, 2]
"""

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        if nums is None or len(nums) < 2:
            return None
        start = 0
        end = len(nums) - 1
        pairs = []
        while start < end:
            if nums[start] + nums[end] == target:
                pairs.append(start+1)
                pairs.append(end+1)
                return pairs
            if nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return pairs