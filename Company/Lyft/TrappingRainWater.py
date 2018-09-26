"""
LeetCode 42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

"""
1. Leftmost and rightmost wall determine the base
2. Shorter wall determine the max height
"""

""" Method 1: Two pointers """
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        water = 0

        if left >= right:
            return water

        leftHeight = height[left]
        rightHeight = height[right]

        while left < right:
            # if left is shorter, water flow from left
            if leftHeight < rightHeight:
                left += 1
                # compare leftmost height and curr height:
                if leftHeight > height[left]:
                    # Then fill water!
                    water += leftHeight - height[left]
                else: # update leftmost height
                    leftHeight = height[left]
            else: #right is shorter, water from right
                right -= 1
                if rightHeight > height[right]:
                    water += rightHeight - height[right]
                else:
                    rightHeight = height[right]
        return water
