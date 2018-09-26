"""
59. 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers.

Example
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Challenge
O(n^2) time, O(1) extra space
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # check corner case
        if numbers is None or len(numbers) < 3:
            return -1

        numbers.sort()
        best_sum = numbers[0] + numbers[1] + numbers[2]
        for i in range(len(numbers)):
            # two pointers
            start, end = i + 1, len(numbers) - 1
            while start < end:
                sum = numbers[i] + numbers[start] + numbers[end]
                # compare with best sum
                if abs(target - sum) < abs(target - best_sum):
                    best_sum = sum
                # move pointers
                if sum < target:
                    start += 1
                else:
                    end -= 1
        return best_sum