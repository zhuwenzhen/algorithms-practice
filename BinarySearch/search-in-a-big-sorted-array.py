"""
447. Search in a Big Sorted Array
Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn't exist in the array.

Example
Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.

Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.

Challenge
O(log k), k is the first index of the given target number.

给一个按照升序排序的正整数数组。这个数组很大以至于你只能通过固定的接口 ArrayReader.get(k) 来访问第k个数。
或者C++里是ArrayReader->get(k))，并且你也没有办法得知这个数组有多大。
找到给出的整数target第一次出现的位置。你的算法需要在O(logk)的时间复杂度内完成，k为target第一次出现的位置的下标。
如果找不到target，返回-1。
"""


class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    """
    首先设，index = 1 之后两倍的扩大。
    注意 index 要从 0 开始，注意！！！index翻倍后要-1
    还有while 的循环条件 start + 1 < end;
    """
    def searchBigSortedArray(self, reader, target):
        index = 1
        while reader.get(index - 1) < target:
            index = index * 2

        start, end = 0, index
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) >= target:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1