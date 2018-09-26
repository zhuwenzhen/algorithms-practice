"""
544. Top k Largest Numbers
Given an integer array, find the top k largest numbers in it.
Example
Given [3,10,1000,-99,4,100] and k = 3.
Return [1000, 100, 10].
"""

import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        res = []
        for i in range(k):
            res.append(-1 * heapq.heappop(heap))
        return res

    def topk2(self, nums, k):
        heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        return topk

nums = [3,10,1000,-99,4,100]
s = Solution()
print(s.topk(nums, 3))