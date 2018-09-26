"""
364. Trapping Rain Water II
Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.



Example
Given 5*4 matrix

[12,13,0,12]
[13,4,13,12]
[13,8,10,12]
[12,13,12,12]
[13,13,13,13]
return 14.

"""

import heapq

class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        if not heights: return 0

        m, n = len(heights), len(heights[0])
        # Use visited to mark the outside
        visited = [ [0 for _ in range(n)] for _ in range(m)]
        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        heap = [] # min heap
        for i in range(m):
            heapq.heappush(heap, (heights[i][0], i, 0))
            visited[i][0] = 1
            heapq.heappush(heap, (heights[i][n-1], i, n-1))
            visited[i][n-1] = 1

        for i in range(n):
            heapq.heappush(heap, (heights[0][i], 0, i))
            visited[0][i] = 1
            heapq.heappush(heap, (heights[m-1][i], m-1, i))
            visited[m-1][i] = 1

        # Start from the current lowest (min pts)
        water = 0
        while heap:
            h, x, y = heapq.heappop(heap)
            for dx, dy in offsets:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    nh = max(h, heights[nx][ny])
                    heapq.heappush(heap, (nh, nx, ny))
                    if h > heights[nx][ny]:
                        water += h - heights[nx][ny]

        return water

heights = [[12,13,0,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
s = Solution()
print(s.trapRainWater(heights))