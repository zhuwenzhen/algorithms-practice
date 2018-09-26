"""
81. Find Median from Data Stream
Numbers keep coming, return the median of numbers at every time a new number added.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].

Challenge
Total run time in O(nlogn).
"""
import heapq

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    minHeap, maxHeap = [], []
    numbers = 0
    def medianII(self, nums):
        res = []
        for num in nums:
            self.add(num)
            res.append(self.getMedian())
        return res


    def add(self, value):
        print("minHeap", self.minHeap)
        print("maxHeap", self.maxHeap)
        if self.numbers % 2 == 0: # even amount of numbers
            heapq.heappush(self.maxHeap, -value)
        else: # odd amount of numbers
            heapq.heappush(self.minHeap, value)

        self.numbers += 1

        if not self.minHeap or not self.maxHeap:
            return

        if -self.maxHeap[0] > self.minHeap[0]: # maximum in maxHeap > minimum in minHeap
            maxroot = -self.maxHeap[0]
            minroot = self.minHeap[0]
            heapq.heapreplace(self.maxHeap, -minroot)
            heapq.heapreplace(self.minHeap, maxroot)

    def getMedian(self):
        return -self.maxHeap[0] # return the root of maxheap

s = Solution()
nums = [4, 5, 1, 3, 2, 6, 0]
print("Return", s.medianII(nums))
