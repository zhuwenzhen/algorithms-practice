"""
1374. Shortest Distance in 3D Space
Given an integer N represents an N*N*N space, and an array of coordinates represents the position of the barrier, return the minimum number of steps from (0,0,0) to (n-1,n-1,n-1), if you can't reach (n-1,n-1,n-1), return -1.

Example
Example 1:

Input: N = 3, barrier = [[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1,1],[1,1,2],[1,2,1],[1,2,2]]
Output: 6
Example 2:

Input: N = 3, barrier = [[2,2,2]]
Output: -1
"""
# import collections
#
# class Solution:
#     """
#     @param N: the size of space
#     @param barriers: an array of coordinates represents the position of the barrier
#     @return: the minimum number of steps
#     """
#     def shortestDistance(self, N, barriers):
#         # Use BFS
#         if N == 0: return 0
#         queue = []
#         wall = dict()
#         for x, y, z in barriers:
#             wall[(x, y, z)] = True
#
#         if (0, 0, 0) in wall or (N - 1, N - 1, N - 1) in wall:
#             return -1
#
#         queue.append((0, 0, 0, 0))
#         visited = set()
#         visited.add((0,0,0))
#
#         dx = [1, -1, 0, 0, 0, 0]
#         dy = [0, 0, 1, -1, 0, 0]
#         dz = [0, 0, 0, 0, 1, -1]
#
#         while queue:
#             x, y, z, steps = queue.pop()
#
#             if (x, y, z) == (N - 1, N - 1, N -1):
#                 return steps
#
#             for i in range(6):
#                 nx, ny, nz = x + dx[i], y + dy[i],  z + dz[i]
#                 print(nx, ny, nz)
#                 if nx >= 0 and nx < N and ny >= 0 and ny < N and nz >= 0 and nz < N and (nx, ny, nz) not in visited:
#                     visited.add((nx, ny, nz))
#                     if (nx, ny, nz) == (N - 1, N - 1, N -1):
#                         return steps + 1
#                     elif (nx, ny, nz) not in wall:
#                         queue.append((nx, ny, nz, steps + 1))
#         return -1

import collections

class Solution:
    """
    @param N: the size of space
    @param barriers: an array of coordinates represents the position of the barrier
    @return: the minimum number of steps
    """

    def shortestDistance(self, N, barriers):
        # Use BFS
        if N == 0: return 0
        queue = collections.deque()
        wall = dict()
        for x, y, z in barriers:
            wall[(x, y, z)] = True

        if (0, 0, 0) in wall or (N - 1, N - 1, N - 1) in wall:
            return -1

        queue.append((0, 0, 0, 0))
        visited = set()
        visited.add((0, 0, 0))

        dx = [1, -1, 0, 0, 0, 0]
        dy = [0, 0, 1, -1, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]

        while queue:
            x, y, z, steps = queue.popleft()

            if (x, y, z) == (N - 1, N - 1, N - 1):
                return steps

            for i in range(6):
                nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

                if nx >= 0 and nx < N and ny >= 0 and ny < N and nz >= 0 and nz < N and (nx, ny, nz) not in visited:
                    visited.add((nx, ny, nz))
                    if (nx, ny, nz) == (N - 1, N - 1, N - 1):
                        return steps + 1
                    elif (nx, ny, nz) not in wall:
                        queue.append((nx, ny, nz, steps + 1))
        return -1

barrier = \
    [[1, 0, 0], [1, 0, 1], [1, 0, 2],
     [1, 1, 0], [1, 1, 1], [1, 1, 2],
     [1, 2, 1], [1, 2, 2]]
# barrier = [[2,2,2]]
N = 3

s = Solution()
print(s.shortestDistance(N, barrier))