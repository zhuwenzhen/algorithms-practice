"""
31. Partition Array
Given an array nums of integers and an int k,
partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

Example
If nums = [3,2,2,1] and k=2, a valid answer is 1.

Challenge
Can you partition the array in-place and in O(n)?
"""

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if nums is None or not nums:
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left

s = Solution()
nums = [9,9,9,8,9,8,7,9,8,8,8,9,8,9,8,8,6,9]
k = 9
# all elem < 3 are moved to left
# all elem >= 3 are moved to right
# [1, 2, 2, 3, 4, 5]
print(s.partitionArray(nums, k))
