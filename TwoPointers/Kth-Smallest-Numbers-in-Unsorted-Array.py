"""
461. Kth Smallest Numbers in Unsorted Array
Find the kth smallest numbers in an unsorted integer array.

Example
Given [3, 4, 1, 2, 5], k = 3, the 3rd smallest numbers are [1, 2, 3].

Challenge
An O(nlogn) algorithm is acceptable, if you can do it in O(n), that would be great.
"""

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        if nums is None or not nums: return -1
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)

    # O(n)
    # T(n) = O(n) + T(n/2) = O(n) + O(n/2) + O(n/4) + ... + O(1) = O(n)
    # Worst case: Everytime O(n) -> O(n - 1)
    def quickSelect(self, A, start, end, k):
        if start == end:
            return A[start]

        # Partition
        left, right = start, end
        pivot = A[ (start + end) // 2]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1
            while left <= right and A[right] > pivot:
                right -= 1
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1

        # start ----k?--- right ---k?--- left ---k?---- end

        if right >= k and start <= right:
            return self.quickSelect(A, start, right, k)
        elif left <= k and left <= end:
            return self.quickSelect(A, left, end, k)
        else:
            return A[k]