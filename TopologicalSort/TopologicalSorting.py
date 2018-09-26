"""
127. Topological Sorting
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.

Example
For graph as follow:

picture

The topological order can be:

[0, 1, 2, 3, 4, 5]
[0, 2, 3, 1, 5, 4]
...
Challenge
Can you do it in both BFS and DFS?
"""
import queue
"""
Definition for a Directed graph node
"""
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        res = []
        map = {} # node -> nodeLabel
        for node in graph:
            for neighbor in node.neighbors:
                if neighbor in map:
                    map[neighbor] = map[neighbor] + 1
                else:
                    map[neighbor] = 1

        q = queue.Queue()
        for node in graph:
            if node not in map:
                q.put(node)
                res.append(node)

        while not q.empty():
            node = q.get()
            for neighbor in node.neighbors:
                map[neighbor] = map[neighbor] - 1
                if map[neighbor] == 0:
                    res.append(neighbor)
                    q.put(neighbor)
        return res




