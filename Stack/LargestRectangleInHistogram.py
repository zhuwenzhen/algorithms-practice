"""
122. Largest Rectangle in Histogram
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

histogram

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

histogram

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example
Given height = [2,1,5,6,2,3],
return 10.
"""
class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
    def largestRectangleArea(self, height):
        i = 0
        area = 0
        stack = []
        while i < len(height):
            #curr = height[i]
            if not stack or height[i] > height[stack[-1]]: # curr > stack.peek()
                stack.append(i)
            else: # stack is empty and curr < stack[peek
                curr = stack.pop()
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                area = max(area, width * height[curr])

                i -= 1
            i += 1

        while stack:
            curr = stack.pop()
            if not stack:
                width = i
            else:
                width = len(height) - stack[-1] - 1
            area = max(area, width * height[curr])
        return area

s = Solution()
heights = [2,1,5,6,2,3]
print(s.largestRectangleArea(heights))


