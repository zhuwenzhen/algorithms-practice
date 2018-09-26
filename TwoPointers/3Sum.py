"""
57. 3Sum
Given an array S of n integers,
are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
"""


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, nums):
        # write your code here
        nums.sort()
        res = []
        length = len(nums)

        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -1 * nums[i]
            start = i + 1
            end = length - 1
            while (start < end):
                if nums[start] + nums[end] == target:
                    res.append([nums[i], nums[start], nums[end]])
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
        return res