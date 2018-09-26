
"""
604. Window Sum
Given an array of n integer, and a moving window(size k),
move the window at each iteration from the start of the array,
find the sum of the element inside the window at each moving.

Example
For array [1,2,7,8,5], moving window size k = 3.
1 + 2 + 7 = 10
2 + 7 + 8 = 17
7 + 8 + 5 = 20
return [10,17,20]
"""

# 同向双指针
# 两根指针一前一后，直到前面的指针走过头 时间复杂度 O(n)
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        n = len(nums)
        if n < k or k <= 0 or len(nums) == 0:
            return []
        sums = [0] * (n - k + 1)
        for i in range(k):
            sums[0] += nums[i]
        for i in range(1, n-k+1):
            sums[i] = sums[i-1] - nums[i-1] + nums[i+k-1]
        return sums