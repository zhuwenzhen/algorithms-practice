"""
Equations are given in the format A / B = k,
where A and B are variables represented as strings,
and k is a real number (floating point number).
Given some queries, return the answers.
If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].


a / c = a / b * b / c
Use DFS to find such a chain:
a / c = a / x1 x2/x3 ... xn / c
"""

# http://zxi.mytechroad.com/blog/graph/leetcode-399-evaluate-division/

import collections
class Solution:
    def divide(self, x, y, visited, g):
        if x == y: return 1.0
        visited.add(x)
        for n in g[x]:
            if n in visited: continue
            visited.add(n)
            d = self.divide(n, y, visited, g)
            if d > 0: return d * g[x][n]
        return -1.0

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # build graph
        g = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            g[x][y] = v
            g[y][x] = 1.0 / v

        ans = []
        for x, y in queries:
            if x in g and y in g:
                ans.append(self.divide(x, y, set(), g))
            else:
                ans.append(-1)
        return ans

class UF:
    def calcEquation(self, equations, values, queries):
        uf = {}
        def find(x):
            if x != uf[x][0]:
                px, pv = find(uf[x][0])
                uf[x] = (px, uf[x][1] * pv)
            return uf[x]

        def divide(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry: return -1.
            return vx / vy

        for (x, y), v in zip(equations, values):
            if x not in uf and y not in uf:
                uf[x] = (y, v)
                uf[y] = (y, 1.)
            elif x not in uf:
                uf[x] = (y, v)
            elif y not in uf:
                uf[y] = (x, 1.0 / v)
            else:
                rx, vx = find(x)
                ry, vy = find(y)
                uf[rx] = (ry, v / vx * vy)

        res = [divide(x, y) if x in uf and y in uf else -1 for x, y in queries]
        return res



s = Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

print(s.calcEquation(equations, values, queries))