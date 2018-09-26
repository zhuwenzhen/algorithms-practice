"""
432. Find the Weak Connected Component in the Directed Graph
Find the number Weak Connected Component in the directed graph.
Each node in the graph contains a label and a list of its neighbors.
(a connected set of a directed graph is a subgraph in which
any two vertices are connected by direct edge path.)

Example
Given graph:
A----->B  C
 \     |  |
  \    |  |
   \   |  |
    \  v  v
     ->D  E <- F

Return {A,B,D}, {C,E,F}.
Since there are two connected component which are {A,B,D} and {C,E,F}
"""

"""

"""

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class UnionFind:
    def __init__(self, nodes):
        self.father = {}
        for i in range(len(nodes)):
            self.father[nodes[i].label] = nodes[i].label

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y

class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet2(self, nodes):
            uf = UnionFind(nodes)
            for node in nodes:
                for neighbor in node.neighbors:
                    uf.union(node.label, neighbor.label)

            hash = {}
            for node in nodes:
                root_label = uf.find(node.label)
                if root_label not in hash:
                    hash[root_label] = []
                hash[root_label].append(node.label)

            res = []
            for _, node in hash.items():
                res.append(node)

            return list(map(sorted, list(map(set, res))))

