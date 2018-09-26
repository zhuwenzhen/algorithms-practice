"""

612. K Closest Points
Given some points and a point origin in two dimensional space,
find k points out of the some points which are nearest to origin.
Return these points sorted by distance,
if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.

Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
"""

"""
Definition for a point.
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

import heapq

class Type:
    def __init__(self, d, p):
        self.d = d
        self.p = p

    # note that __lt__ in python 3 and __cmp__ in python 2
    def __lt__(self, other):
        if other.d != self.d:
            return other.d > self.d
        if other.p.x != self.p.x:
            return other.p.x > self.p.x
        return other.p.y > self.p.y

class Solution:
    def distance(self, A, B):
        return ((A.x - B.x)**2 + (A.y - B.y)**2)

    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        heap = []
        for p in points:
            dist = self.distance(p, origin)
            heapq.heappush(heap, Type(dist, p))
            # Pop and return the smallest item from the heap, maintaining the heap invariant.
            if len(heap) > k:
                l = heapq.heappop(heap)
                print("pop out", l.p.x, l.p.y)
        res = []
        while heap:
            res.append(heapq.heappop(heap).p)
        res.reverse()
        return res

points = [[4,6],[4,7],[4,4],[2,5],[1,1]]
pts = [Point(x, y) for x, y in points]
origin = Point(0,0)

s = Solution()
res = s.kClosest(pts, origin, 3)
for i in res:
    print(i.x, i.y)

    """
    
    def kClosest(self, points, origin, k):
        heap = []
        for p in points:
            dist = self.distance(p, origin)
            heapq.heappush(heap, Type(dist, p))

            # Pop and return the smallest item from the heap, maintaining the heap invariant.
            # if len(heap) > k:
            #     heapq.heappop(heap)
        # for h in heap:
        #     print("(", h.p.x,",",h.p.y, "), d =", h.d)
        res = []
        for i in range(k):
            # Pop and return the smallest item from the heap, maintaining the heap invariant.
            res.append(heapq.heappop(heap).p)
            
        return res
    """






