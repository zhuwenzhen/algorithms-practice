"""
406. Minimum Size Subarray Sum
Given an array of n positive integers and a positive integer s,
find the minimal length of a subarray of which the sum ≥ s.
If there isn't one, return -1 instead.

Example
Given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

Challenge
If you have figured out the O(n) solution,
try coding another solution of which the time complexity is O(n log n).
"""

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        sum = 0
        res = 1e10
        n = len(nums)
        l = 0
        for r in range(n):
            sum += nums[r]
            while sum >= s:
                res = min(res, r - l + 1)
                sum -= nums[l]
                l += 1

        if res == 1e10: return -1
        else: return res

arr = [2,3,1,2,4,3]
target = 7

s = Solution()
print(s.minimumSize(arr, target))