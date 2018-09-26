"""
4. Ugly Number II
Ugly number is a number that only have factors 2, 3 and 5.
Design an algorithm to find the nth ugly number.
The first 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12...

Example
If n=9, return 10.
Challenge
O(n log n) or O(n) time.
"""
import heapq

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        if n <= 1:
            return n

        n -= 1
        key = [2, 3, 5]
        heap = []

        for i in range(3):
            heapq.heappush(heap, (key[i], i))
        value = key[0]

        while n > 0:
            value, level = heapq.heappop(heap)
            while level < 3:
                new_value = key[level] * value
                heapq.heappush(heap, (new_value, level))
                level += 1
            n -= 1
        return value



