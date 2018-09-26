"""
137. Clone Graph
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

How we serialize an undirected graph:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

   1
  / \
 /   \
0 --- 2
     / \
     \_/

"""
"""
Definition for a undirected graph node
"""

import collections

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        root = node
        if node is None:
            return node

        # use bfs to traverse the graph and get all nodes
        nodes = self.getNodes(node)
        # old -> new mapping info in hashmap
        mapping = {}
        for n in nodes:
            mapping[n] = UndirectedGraphNode(n.label)

        # copy neighbors (edges)
        for n in nodes:
            new_node = mapping[n]
            for neighbor in n.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
        return mapping[root]

    def getNodes(self, node):
        q = collections.deque([node])
        res = set([node])

        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in res:
                    res.add(neighbor)
                    q.append(neighbor)
        return res

