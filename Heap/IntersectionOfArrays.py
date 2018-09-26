"""
486. Merge K Sorted Arrays
Given k sorted integer arrays, merge them into one sorted array.

Example
Given 3 sorted arrays:

[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].

Challenge
Do it in O(N log k).

N is the total number of integers.
k is the number of arrays.
"""

"""
基于 Priority Queue 的版本。
假设每个数组长度为 n, 一共 k 个数组。
时间复杂度为 O(k n logn + nklogk)
其中 knlogn 是 k 个数组进行分别排序的时间复杂度
nklogk 是 总共 nk 个数从 PriorityQueue 中进出，每次进出 logk。

相比使用 HashMap 的算法的时间复杂度 O(nk) 这个方法并没有什么时间上的优势。
但是这个方法的空间复杂度很低，只有 O(k)，即多少个数组就花费多少的额外空间。

在面试中也是很有可能会被要求不用 HashMap 或者实现一个比 O(n) 更低的空间复杂度的算法。因此这个程序的方法也是需要掌握的。
"""

import heapq

class Type(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        pass


class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArraysHeap(self, arrs):
        heap = []

        for i in range(len(arrs)):
            if not arrs[i]: return 0
            arrs[i].sort() # k log k
            heapq.heappush(heap, Type(i, 0))

        lastValue = 0
        count = 0
        intersection = 0
        while heap:
            pair = heapq.heappop(heap)
            if arrs[pair.x][pair.y] != lastValue or count == 0:
                if count == len(arrs):
                    intersection += 1
                lastValue = arrs[pair.x][pair.y]
                count = 1
            else:
                count += 1
            pair.y += 1
            if pair.x < len(arrs[pair.x]):
                heapq.heappop(heap)
        # kick out the last element
        if count == len(arrs):
            intersection += 1
        return intersection

    def intersectionOfArrays(self, arrs):
        if arrs is None or not arrs:
            return []
        if not arrs[0]:
            return []

        res = []
        for item in set(arrs[0]):
            for i in range(1, len(arrs)):
                if not item in arrs[i]:
                    break
            else:
                res.append(item)

        return len(res)



s = Solution()
arrs = [[1,30,2,38,55,25,84,92,90,22,45,76,46,47,65,80,69,57,95,88,32,91,43,34,21,72,16,58,75,59,98,79,48,63,6,4,93,20,62,70,53,36,26,41,54,61,87,14,66,31],
        [63,56,80,27,42,99,8,3,77,52,39,1,25,81,21,93,64,69,7,9,57,48,75,24,11,45,13,4,54,96,98,90,32,94,38,40,68,15,2,43,33,22,23,60,72,0,50,89,84,44],
        [88,51,79,67,87,57,14,58,23,16,4,15,32,38,26,56,69,35,97,20,42,31,33,93,89,96,8,59,82,90,10,7,80,30,37,91,71,18,19,52,60,28,24,6,41,39,46,11,47,77],
        [52,12,75,35,33,56,70,77,54,65,15,71,66,37,26,34,20,6,16,55,50,46,28,87,38,29,44,73,5,27,42,11,91,84,94,78,61,25,92,9,97,18,30,69,45,40,82,49,7,95],
        [51,27,86,61,77,53,59,58,32,89,6,62,31,85,40,3,67,33,66,83,37,75,99,72,73,14,47,15,91,96,16,44,26,30,42,46,35,90,79,55,98,19,94,18,52,21,34,10,2,24],
        [71,68,28,0,80,53,45,75,26,37,48,25,19,49,73,57,34,87,79,77,9,12,33,10,50,8,22,21,64,97,4,52,85,86,32,41,43,66,36,54,65,96,7,42,89,17,5,44,55,92],
        [26,46,4,73,5,49,80,8,24,63,31,59,64,74,70,47,78,17,38,99,81,87,29,50,91,67,77,69,21,60,33,98,27,66,53,34,94,79,83,7,72,25,89,58,96,45,10,62,36,19],
        [13,33,78,90,76,60,43,15,36,89,47,50,11,73,20,75,91,44,59,79,39,81,38,31,41,24,63,25,65,51,1,95,83,21,96,80,92,49,32,7,86,19,37,67,56,97,54,29,0,45],
        [34,1,66,26,59,73,77,10,15,9,96,82,74,45,90,3,28,84,88,83,42,46,52,67,85,33,32,8,43,99,25,19,86,95,70,57,92,69,16,35,87,23,64,21,61,97,58,94,55,93],
        [79,60,15,54,77,19,0,85,3,13,82,70,75,81,29,31,26,57,80,38,23,40,84,14,69,45,99,53,98,51,1,35,55,94,18,42,56,25,96,2,97,73,37,46,21,4,64,67,20,43]]
print(s.intersectionOfArrays(arrs))
print(s.intersectionOfArrays2(arrs))