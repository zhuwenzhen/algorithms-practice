"""
65. Median of two Sorted Arrays
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.

Given A=[1,2,3] and B=[4,5], the median is 3.

Challenge
The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def median(self, l):
        if l is None or not l:
            return None
        n = len(l)
        index = (n - 1) // 2
        if (n % 2):
            return l[index]
        else:
            return (l[index] + l[index + 1]) / 2.0

    def findMedianSortedArrays(self, A, B):
        merged = sorted(A + B)
        return self.median(merged)

s = Solution()
print(s.findMedianSortedArrays([1,2,3,4],[2, 3]))