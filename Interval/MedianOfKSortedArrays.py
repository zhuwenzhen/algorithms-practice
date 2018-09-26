"""
931. Median of K Sorted Arrays
There are k sorted arrays nums. Find the median of the given k sorted arrays.

Example
Given nums = [[1],[2],[3]], return 2.00.
"""
import sys
class Solution:

    def getTotal(self, nums):
        """
        :param nums: k sorted arrays
        :return: total number of elements in nums
        """
        sum = 0
        n = len(nums)
        for i in range(n):
            sum += len(nums[i])
        return sum

    def findKth(self, nums, k):
        """

        :param nums:
        :param k:
        :return:
        """
        start, end = 0, sys.maxsize()
        while start + 1 < end:
            pass


    def getGreaterOrEqual(self, nums, val):
        """

        :param nums:
        :param val:
        :return:
        """
        if not nums or nums is None:
            return 0

        # binary search
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= val:
                end = mid
            else:
                start = mid

        if nums[start] >= val:
            return len(nums) - start

        if nums[end] >= val:
            return len(nums) - end

        return 0

nums = [[1, 2, 3], [4, 5, 6]]

s = Solution()
print(s.getTotal(nums))
