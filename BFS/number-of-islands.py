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

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])

        if m == 0 or n == 0: return 0
        visited = [[0 for _ in range(n)] for _ in range(m)]

        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] and not visited[row][col]:
                    visited[row][col] = 1
                    self.bfs(row, col, grid, visited)
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
                    visited[nx][ny] = 1
                    q.append((nx, ny))

grid = [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]]

s = Solution()
print(s.numIslands(grid))