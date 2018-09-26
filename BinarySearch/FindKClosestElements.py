"""
460. Find K Closest Elements
Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.

Example
Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].

Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

Challenge
O(logn + k) time complexity.
"""

class BinarySearch:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        if k <= 0 or not A:
            return []
        res = []
        for i in range(k):
            res.append(A.pop(self.findPosition(A, target)))
        return res

    def findPosition(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        if abs(target - A[start]) <= abs(target - A[end]):
            return start
        else:
            return end

import heapq
class Type:
    def __init__(self, index, val):
        self.index = index
        self.value = val

    def __lt__(self, other):
        if other.value != self.value:
            return other.value > self.value
        else:
            return other.index > self.index


class Solution:
    def kClosestNumbers(self, A, target, k):
        if k <= 0 or not A:
            return []

        heap = []
        for i in range(len(A)):
            diff = abs(A[i] - target)
            heapq.heappush(heap, Type(i, diff))

        ans = []
        for i in range(k):
            t = heapq.heappop(heap)
            ans.append(A[t.index])
        return ans

s = Solution()
s.kClosestNumbers([1, 4, 6, 8], 3, 3)

