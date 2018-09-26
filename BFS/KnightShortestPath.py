"""
611. Knight Shortest Path
Given a knight in a chessboard
(a binary matrix with 0 as empty and 1 as barrier) with a source position,
find the shortest path to a destination position,
return the length of the route.
Return -1 if knight can not reached.

Example
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 2

[[0,1,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return 6

[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2] return -1
"""

"""
Definition for a point.
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


import queue
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        if not grid or grid is None: return -1
        if not grid[0]: return -1
        if grid[source.x][source.y] or grid[destination.x][destination.y]:
            return -1

        m, n = len(grid), len(grid[0])

        dx = [1, 1, -1, -1, 2, 2, -2, -2]
        dy = [2, -2, 2, -2, 1, -1, 1, -1]

        visited = [[0 for _ in range(n)] for _ in range(m)]
        q = queue.Queue(maxsize= n * m)
        q.put(source)
        visited[source.x][source.y] = 1
        steps = 0

        while not q.empty():
            steps += 1
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                for j in range(8):
                    nx = curr.x + dx[j]
                    ny = curr.y + dy[j]
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and not grid[nx][ny] :
                        if nx == destination.x and ny == destination.y:
                            return steps
                        visited[nx][ny] = 1
                        q.put(Point(nx,ny))
        return -1

class Solution2:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path
    def shortestPath(self, grid, source, destination):
        # Write your code here
        n = len(grid)
        m = len(grid[0])

        import sys
        record = [[sys.maxsize for _ in range(m)] for _ in range(n)]
        record[source.x][source.y] = 0

        import queue
        q = queue.Queue(maxsize = n * m)
        q.put(source)

        d = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
        while not q.empty():
            head = q.get()
            for dx, dy in d:
                x, y = head.x + dx, head.y + dy
                if x >=0 and x < n and y >= 0 and y < m and not grid[x][y] and \
                    record[head.x][head.y] + 1 < record[x][y]:
                    record[x][y] = record[head.x][head.y] + 1
                    q.put(Point(x, y))

        if record[destination.x][destination.y] == sys.maxsize:
            return -1

        return record[destination.x][destination.y]

grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]
source = Point(2, 0)
destination = Point(2, 2)

grid = [[0,0,0,0,1,1],
        [1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,1,0,1],[1,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1],[0,0,1,0,0,1]]
source = Point(0,0)
destination = Point(7,0)
s = Solution()
s2 = Solution2()
print(s.shortestPath(grid, source, destination))
print(s2.shortestPath(grid, source, destination))