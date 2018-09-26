"""
144. Interleaving Positive and Negative Numbers
Given an array with positive and negative integers.
Re-range it to interleaving with positive and negative integers.

Example
Given [-1, -2, -3, 4, 5, 6], after re-range,
it will be [-1, 5, -2, 4, -3, 6] or any other reasonable answer.

Challenge
Do it in-place and without extra memory.
"""


class Solution:
    def rerange(self, nums):
        """
        :type nums: list[int]
        :rtype: void
        """
        if not nums or len(nums) == 1:
            return

        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            while left < right and nums[left] < 0:
                left += 1
            while left < right and nums[right] > 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if left > n - left:
            self.interleave(nums, 1, n - 1)
        elif left < n - left:
            self.interleave(nums, 0, n - 2)
        else:
            self.interleave(nums, 0, n - 1)

    def interleave(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 2
            right -= 2


            
class Solution:
    """
    @param A: An integer array.
    @return nothing
    """
    def subfun(self, A, B):
        ans = []
        for i in range(len(B)):
            ans.append(A[i])
            ans.append(B[i])
        if(len(A) > len(B)):
            ans.append(A[-1])
        return ans
    def rerange(self, A):
        Ap = [i for i in A if i > 0]
        Am = [i for i in A if i < 0]
        if(len(Ap) > len(Am)):
            tmp = self.subfun(Ap, Am)
        else:
            tmp = self.subfun(Am, Ap)
        for i in range(len(tmp)):
            A[i] = tmp[i]