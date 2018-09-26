"""
1298. Minimum Height Trees
For a undirected graph with tree characteristics,
we can choose any node as the root. The result graph is then a rooted tree.
Among all possible rooted trees,
 those with minimum height are called minimum height trees (MHTs).
 Given such a graph, write a function to find all the MHTs
 and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1.
You will be given the number n and a list of undirected edges
(each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0]
and thus will not appear together in edges.

Example
Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
"""

class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """
    def findMinHeightTrees(self, n, edges):

        if not edges or edges is None:
            return [0]

        hs = {}
        for e in edges:
            hs[e[0]] = []
            hs[e[1]] = []

        degree_table = {}
        for e in edges:
            hs[e[0]].append(e[1])
            hs[e[1]].append(e[0])

        for v, neighbors in hs.items():
            degree_table[v] = len(neighbors)

        # take out the leaves until there are only 1 or 2 nodes left
        while len(degree_table) > 2:
            for v, deg in list(degree_table.items()):
                if deg == 1: # remove leaves
                    del degree_table[v]

        # print(degree_table)
        return list(degree_table.keys())

    def findMinHeightTrees2(self, n, edges):
        if n < 2:
            return [0]

        graph = [set() for _ in range(n)]
        for item in edges:
            graph[item[0]].add(item[1])
            graph[item[1]].add(item[0])

        print("graph", graph)

        leaves = [i for i in range(n) if len(graph[i]) == 1]
        print("leaves", leaves)

        while (n > 2):
            new_leaves = set()
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.add(neighbor)
                n -= 1
            leaves = new_leaves
            print("new leaves", new_leaves)
        return list(leaves)


s = Solution()
print(s.findMinHeightTrees2(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
edges = [[1, 0], [1, 2], [1, 3]]
n = 4
print(s.findMinHeightTrees2(n, edges))