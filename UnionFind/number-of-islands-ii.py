"""
434. Number of Islands II
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. Return how many island are there in the matrix after each operator.

Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].
"""

class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

class UnionFind:
    def __init__(self, n, m):
        self.father = {}
        for i in range(n):
            for j in range(m):
                id = self.convertId(i, j, m)
                self.father[id] = id

    def convertId(self, x, y, m):
        return x * m + y

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
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    def numIslands2(self, n, m, operators):
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        uf = UnionFind(n, m)
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]

        res = []
        count = 0
        for point in operators:
            x, y = point.x, point.y
            if matrix[x][y] != 1:
                count += 1
                matrix[x][y] = 1
                id = uf.convertId(x, y, m)
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx and nx < n and 0 <= ny and ny < m and matrix[nx][ny] == 1:
                        new_id = uf.convertId(nx, ny, m)
                        root_id = uf.find(id)
                        root_new_id = uf.find(new_id)
                        if root_id != root_new_id:
                            count -= 1
                            uf.union(root_id, root_new_id)
            res.append(count)
        return res

s = Solution()
op = [[0,0],[0,1],[2,2],[2,1]]
ops = []
for p in op:
    ops.append(Point(p[0], p[1]))

print(s.numIslands2(3, 3, ops))