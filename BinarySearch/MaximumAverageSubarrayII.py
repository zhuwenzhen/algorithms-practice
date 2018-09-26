"""
617. Maximum Average Subarray II
Given an array with positive and negative numbers,
find the maximum average subarray which length
should be greater or equal to given length k.

Example
Given nums = [1, 12, -5, -6, 50, 3], k = 3

Return 15.667 // (-6 + 50 + 3) / 3 = 15.667
"""

class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        start = -1e6
        end = 1e6
        eps = 1e-6

        while start + eps < end:
            mid = start + (end - start) / 2
            print(mid)
            if self.checkAvg(nums, mid, k):
                start = mid
            else:
                end = mid
        return start

    def checkAvg(self, nums, avg, k):
        sums, preSum, preMin = 0, 0, 0
        # preMin is the minimum value of preSum
        # sums - preMin will give the possible maximum of the subarray

        for i in range(len(nums)):
            sums += nums[i] - avg

            if i >= k - 1 and sums >= 0:
                return True

            # sums is the sum of all the elements from 0 to i
            # preSum is the sum of all the elements from 0 to i - k
            # then we can guarentee the array of sums - preSum is greater than k

            if i >= k:
                preSum += nums[i - k] - avg
                prevMin = min(preMin, preSum)
                if sums - prevMin >= 0:
                    return True
        return False

nums = [-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-4,5,-1000]

s = Solution()
print(s.maxAverage(nums, 10))