"""

143. Sort Colors II
Given an array of n objects with k different colors (numbered from 1 to k),
sort them so that objects of the same color are adjacent,
with the colors in the order 1, 2, ... k.

Example
Given colors=[3, 2, 2, 1, 4], k=4,
your code should sort colors in-place to [1, 2, 2, 3, 4].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
That will cost O(k) extra memory. Can you do it without using extra memory?
"""

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        i = 0
        n = len(colors)
        while i < n:
            if colors[i] > 0:
                if colors[colors[i]-1] > 0:
                    tmp = colors[i]
                    colors[i] = colors[colors[i]-1]
                    colors[tmp-1] = -1
                    i = i - 1
                else:
                    colors[colors[i]-1] -= 1
                    colors[i] = 0
            i = i + 1

        i = len(colors)-1
        k = i
        while i >= 0:
            if colors[i] < 0:
                pos = k + colors[i]
                while k > pos:
                    colors[k] = i+1
                    k -= 1
            i -= 1