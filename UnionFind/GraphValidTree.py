"""
178. Graph Valid Tree
Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
"""

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    """
    1. 初始化Union Find的father map, 让每一个节点的初始parent指向自己, （自己跟自己是一个Group）
    2. 在循环读取edge list时，查找两个节点的parent，如果相同，说明形成了环（Cycle），那么这便不符合树（Tree）的定义
    3. 如果不相同，则将其中一个节点设为另一个的parent，继续循环
    
    此外还有需要注意的是对于vertex和edge的validation，
    |E| = |V| - 1，也就是要验证 edges.length == n，
    如果该条件不满足，则Graph一定不是valid tree。
    """

    def validTree(self, n, edges):
        if len(edges) != n - 1 or n == 0: return False
        father = [i for i in range(n)]
        for e in edges:
            root_a = self.find(e[0], father)
            root_b = self.find(e[1], father)
            if root_a == root_b:
                return False
            else:
                father[root_a] = root_b
        return True

    def find(self, x, father):
        if father[x] == x: return x
        father[x] = self.find(father[x], father)
        return father[x]


sol = Solution()

n = 5
trees = [[0,1],[0,2],[0,3],[1,4]]

print(sol.validTree(n, trees))