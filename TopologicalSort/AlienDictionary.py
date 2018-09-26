"""
892. Alien Dictionary
There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Example
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf"

Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".
"""
import queue
import heapq

class Solution:
    # O(n * k)
    def constructGraph(self, words):
        graph = {} # character -> neighboring chars
        # 1. create nodes
        for i in range(len(words)):
            for j in range(len(words[i])):
                c = words[i][j]
                if c not in graph:
                    graph[c] = []
        # 2. create edges
        for i in range(len(words) - 1):
            index = 0
            while index < len(words[i]) and index < len(words[i + 1]):
                if words[i][index] != words[i+1][index]:
                    graph[words[i][index]].append(words[i+1][index])
                    break
                index += 1
        return graph
        # {'w': ['e'], 'r': ['t'], 't': ['f'], 'f': [], 'e': ['r']}
    def getInDegree(self, graph):
        in_degree = {} # char : in degree
        for c in graph.keys():
            in_degree[c] = 0
        for u in graph.keys():
            for v in graph[u]:
                in_degree[v] += 1
        return in_degree

    def topologicalSorting(self, graph):
        indegree = self.getInDegree(graph)
        heap = []
        for u in indegree.keys():
            if indegree[u] == 0:
                heapq.heappush(heap, u)

        s = ""
        while heap:
            head = heapq.heappop(heap)
            s += head
            for n in graph[head]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    heapq.heappush(heap, n)

        if len(s) != len(indegree):
            return ""
        return s

    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # step 1: construct directed graph with words
        graph = self.constructGraph(words)
        # step 2: run topological sorting on the graph
        return self.topologicalSorting(graph)



words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

words2 = ["zy","zx"]

s = Solution()
graph = s.constructGraph(words2)
print(graph)
print(s.alienOrder(words2))