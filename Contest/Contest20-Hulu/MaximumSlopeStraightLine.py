"""
996. Maximum Slope Straight Line
Given a series of rectangular coordinates
in the integer point (x, y), starting from 0,
the i-th point number is i.
There is no any two points with the same x,
find the number of the two points that can make up
the maximum slope line (a,b)(a,b).
If there is more than one such point pair, return the point pair with the smallest lexicographical order.

Example
Given points=[[0,0],[1,2],[2,3],[3,4]], return [0,1].

Explanation:
The slope of the line formed by the [0,0] point and the [1,2] point is the largest.
Given points=[[0,0],[1,0],[2,0]], return [0,1].

Explanation:
The slope of the line formed by the [0,0] point and the [1,0] point, is equal to the slope of the line formed by the [0,0], [2,0], [1,0] and [2,0] points, but the lexicographic order of [0,1] is less than [0,2] and [1,2].
"""

class Solution:
    """
    @param points: The points set
    @return: Return the point pair
    """
    def getSlope(self, a, b):
        x1, y1= a.x, a,y
        x2, y2 = b.x, b.y
        if x1 != x2:
            return (y2 - y1) / (x2 - x1)
        else:
            return 1e10

    def getPoints(self, points):
        n = len(points)
        if points is None or n == 0:
            return []
        maxSlope = -1e10
        indices = [0, 0]
        for i in range(n-1):
            for j in range(i + 1, n):
                slope = self.getSlope(points[i], points[j])
                if slope > maxSlope:
                    maxSlope = slope
                    indices = [i, j]
        return indices

points=[[-1430,-18732],[-1441,-22482],[-5817,24054],[14741,25893],[-24664,-28094],[29797,17247],[-28277,30109],[13543,18680],[-13399,-13325],[26225,15630]]
s = Solution()
print(s.getPoints(points))