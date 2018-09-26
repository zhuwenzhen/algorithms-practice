"""
431. Connected Component in Undirected Graph
Find the number connected component in the undirected graph.
Each node in the graph contains a label and a list of its neighbors.
(a connected component (or just component) of an undirected graph
is a subgraph in which any two vertices are connected to each other
by paths, and which is connected to no additional vertices in the supergraph.)

Example
Given graph:

A------B  C
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      D   E

Return {A,B,D}, {C,E}.

Since there are two connected component which is {A,B,D}, {C,E}
"""

"""
Definition for a undirected graph node
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
    def connectedSet(self, nodes):
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

        print("res", res)

        return list(map(sorted, list(map(set, res))))





graph_data = "{1,2,4#2,1,4#3,5#4,1,2#5,3}"
vertexStrings = graph_data[1:-1].split("#")
vertices = [v.split(',') for v in vertexStrings]
g = {}
print(vertices)
for v in vertices:
    g[v[0]] = v[1:]

print("graph", g)
test = []
for v, neightbors in g.items():
    node = UndirectedGraphNode(v)
    node.neighbors = [UndirectedGraphNode(n) for n in neightbors]
    test.append(node)

s = Solution()
print(s.connectedSet(test))

