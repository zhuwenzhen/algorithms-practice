"""
41. Maximum Subarray
Given an array of integers,
find a contiguous subarray which has the largest sum.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

Challenge
Can you do it in time complexity O(n)?
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        if nums is None and not nums:
            return 0
        maxNum = -100000
        sum, minSum = 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            maxNum = max(maxNum, sum - minSum)
            minSum = min(minSum, sum)
            print(sum, maxNum, minSum)
        return max

    def kadane(self, nums):
        max_so_far, max_end_here = 0, 0
        for elem in nums:
            max_end_here += elem
            if max_end_here < 0:
                max_end_here = 0
            if max_so_far < max_end_here:
                max_so_far = max_end_here
        return (max_end_here, max_so_far)

    def max_subarray(self, A):
        max_ending_here = max_so_far = A[0]
        for x in A[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


arr = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
s = Solution()
s.maxSubArray(arr)
print(s.max_subarray(arr))