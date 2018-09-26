"""
598. Zombie in Matrix
Given a 2D grid, each cell is either a wall 2,
a zombie 1 or people 0 (the number zero, one, two).
Zombies can turn the nearest people(up/down/left/right) into zombies every day,
but can not through wall.

How long will it take to turn all people into zombies?
Return -1 if can not turn all people into zombies.

Example
Given a matrix:

0 1 2 0 0
1 0 0 2 1
0 1 0 0 0
return 2
"""

ZOMBIE = 1
PEOPLE = 0
WALL = 2


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    def zombie(self, grid):
        if len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        qx = []
        qy = []
        num_people = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == ZOMBIE:
                    qx.append(i)
                    qy.append(j)
                if grid[i][j] == PEOPLE:
                    num_people += 1
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        count = 0
        while qx:
            new_qx = []
            new_qy = []
            for x, y in zip(qx, qy):
                for k in range(4):
                    new_x = x + dx[k]
                    new_y = y + dy[k]
                    if self.valid(grid, new_x, new_y) and grid[new_x][new_y] == PEOPLE:
                        grid[new_x][new_y] = ZOMBIE
                        new_qx.append(new_x)
                        new_qy.append(new_y)
                        num_people -= 1
            qx = new_qx
            qy = new_qy
            count += 1
        if num_people > 0:
            return -1
        return count - 1

    def valid(self, grid, x, y):
        return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])