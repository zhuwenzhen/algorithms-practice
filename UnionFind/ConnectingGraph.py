"""
589. Connecting Graph
Given n nodes in a graph labeled from 1 to n.
There is no edges in the graph at beginning.

You need to support the following method:
+ connect(a, b), add an edge to connect node a and node b.
+ query(a, b), check if two nodes are connected

Example
5 // n = 5
query(1, 2) return false
connect(1, 2)
query(1, 3) return false
connect(2, 4)
query(1, 4) return true
"""



class ConnectingGraph:
    """
    @param: n: An integer
    """

    def __init__(self, n):
        self.parent = [0 for _ in range(n + 1)]

    def find(self, x):
        if self.parent[x] == 0: return x # if x's parent is 0, x is its own parent
        self.parent[x] = self.find(self.parent[x]) # other wise (path compression) x's parent is his ancestor
        return self.parent[x]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b # merge set a and set b by pointing root_a's parent to root_b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """

    def query(self, a, b):
        # find a and b's ancestor
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b

# write your code here


