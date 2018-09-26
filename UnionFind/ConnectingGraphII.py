"""
590. Connecting Graph II

Given n nodes in a graph labeled from 1 to n.
There is no edges in the graph at beginning.
You need to support the following method:
connect(a, b), an edge to connect node a and node b
query(a), Returns the number of connected component nodes which include node a.

Example
5 // n = 5
query(1) return 1
connect(1, 2)
query(1) return 2
connect(2, 4)
query(1) return 3
connect(1, 4)
query(1) return 3
"""

class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.parent = [0 for _ in range(n+1)]
        self.size = [1 for _ in range(n+1)]


    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def find(self, x):
        if self.parent[x] == 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.size[root_b] += self.size[root_a]

    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        root_a = self.find(a)
        return self.size(root_a)

