"""
591. Connecting Graph III
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

You need to support the following method:

connect(a, b), an edge to connect node a and node b
query(), Returns the number of connected component in the graph
Example
5 // n = 5
query() return 5
connect(1, 2)
query() return 4
connect(2, 4)
query() return 3
connect(1, 4)
query() return 3
"""
class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.count = n
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.count -= 1

    """
    @return: An integer
    """
    def query(self):
        return self.count