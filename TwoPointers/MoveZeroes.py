"""
539. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example
Given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].
"""

"""
0 多 vs 0 少 算法有什么区别? 不需要维持相对顺序 vs 需要维持相对顺序 算法有什么区别？ 如果需要保证最少修改次数如何做？
"""
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        if not nums:
            return []
        left, right = 0, 0 # only used two extra variable. O(1) extra space
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
            print(nums)
        return nums
    

s = Solution()

print(s.moveZeroes([0, 1, 2, 3]))