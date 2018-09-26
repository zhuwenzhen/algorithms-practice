"""
363. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

Trapping Rain Water

Example
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

Challenge
O(n) time and O(1) memory
O(n) time and O(n) memory is also acceptable.
"""

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # outside wall determine how much water we can have
        left, right = 0, len(heights) - 1
        water = 0

        if left >= right:
            return water

        left_height = heights[left]
        right_height = heights[right]

        while left < right:
            # if left height is lower, water goes from left to inside
            if left_height < right_height:
                left += 1
                if left_height > heights[left]:
                    water += (left_height - heights[left])
                else:
                    left_height = heights[left]
            else: # water goes from right
                right -= 1
                if right_height > heights[right]:
                    water += (right_height - heights[right])
                else:
                    right_height = heights[right]

        return water