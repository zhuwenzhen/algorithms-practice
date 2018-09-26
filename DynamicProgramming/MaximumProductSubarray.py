"""
191. Maximum Product Subarray
Find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):

        n = len(nums)
        maxs = [0 for _ in range(n)]
        mins = [0 for _ in range(n)]

        # initialization
        maxs[0] = nums[0]
        mins[0] = nums[0]

        res = nums[0]

        for i in range(1, n):
            mins[i] = nums[i]
            maxs[i] = nums[i]
            if nums[i] > 0:
                maxs[i] = max(maxs[i], maxs[i-1] * nums[i])
                mins[i] = min(mins[i], mins[i-1] * nums[i])
            elif nums[i] < 0:
                maxs[i] = max(maxs[i], mins[i-1] * nums[i])
                mins[i] = min(mins[i], maxs[i-1] * nums[i])

            res = max(res, maxs[i])
        return res


    def maxProduct2(self, nums):
        if not nums or nums is None: return 0

        maxProduct = 1
        prod = 1
        for i in range(1, len(nums)):
            if nums[i]*nums[i-1] > prod:
                prod = nums[i]*nums[i-1]
            else:
                prod = 1

            maxProduct = max(maxProduct, prod)
        return maxProduct

s = Solution()

print(s.maxProduct([2, 3, -2, 4]))