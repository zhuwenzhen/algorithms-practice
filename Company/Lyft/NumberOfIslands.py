

"""
433. Number of Islands
Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent, we consider them in the same island. We only consider up/down/left/right adjacent.

Find the number of islands.

Example
Given graph:

[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
return 3.
"""

""" Solution 1: Use BFS """
class BFS:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid: return 0
        if not grid[0]: return 0

        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        count = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] and not visited[x][y]:
                    visited[x][y] = True
                    self.bfs(x, y, grid, visited)
                    count += 1

        return count

    def bfs(self, x, y, grid, visited):
        m, n = len(grid), len(grid[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        q = [(x, y)]
        while q:
            x, y = q.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

""" Solution 2: Use Union Find """
class UnionFind:
    def __init__(self, m, n):
        self.father = {}
        for i in range(m):
            for j in range(n):
                id = self.convertID(i, j, n)
                self.father[id] = id

    def convertID(self, x, y, n):
        return n * x + y

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

class Solution:
    def numIslands(self, grid):
        if not grid: return 0
        if not grid[0]: return 0
        m, n = len(grid), len(grid[0])

        # initialization
        uf = UnionFind(m, n)
        visited = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for x in range(m):
            for y in range(n):
                if grid[x][y] and not visited[x][y]:
                    count += 1
                    visited[x][y] = True
                    id = uf.convertID(x, y, n)
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] and not visited[nx][ny]: # check boundary
                            newID = uf.convertID(nx, ny, n)
                            root_id = uf.find(id)
                            root_newID = uf.find(newID)
                            if root_id != root_newID:
                                count -= 1
                                uf.union(root_id, root_newID)
        return count

grid = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]

grid2 = [[1, 1]]
s = Solution()
print(s.numIslands(grid2))