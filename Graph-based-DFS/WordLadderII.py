"""
121. Word Ladder II
Given two words (start and end), and a dictionary,
find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
"""

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def getEntry(self, word, index):
        return word[:index] + word[index+1:]

    def buildIndices(self, length, dict):
        """
        Build an indices graph for this dictionary
        :param length: start string's len
        :param dict:
        :return:
        """
        indices = []
        for i in range(length):
            index = {}
            for word in dict:
                entry = self.getEntry(word, i)
                words = index.get(entry, [])
                words.append(word)
                index[entry] = words
            indices.append(index)
        return indices

    def getNextWord(self, word):
        nextWords = []
        for i in range(len(word)):
            entry = self.getEntry(word, i)
            if entry in self.indices[i]:
                for nextWord in self.indices[i][entry]:
                    if nextWord != word:
                        nextWords.append(nextWord)
        return nextWords

    def bfs(self, start):
        self.distance = {}
        self.distance[start] = 0
        queue = [start]
        while len(queue) != 0:
            head = queue.pop()
            for word in self.getNextWord(head):
                if word not in self.distance:
                    self.distance[word] = self.distance[head] + 1
                    queue.append(word)

    def dfs(self, curr, target, path):
        if curr == target:
            self.res.append(list(path))
            return

        for word in self.getNextWord(curr):
            if self.distance.get(word, -2) + 1 == self.distance[curr]:
                path.append(word)
                self.dfs(word, target, path)
                del path[-1]

    def findLadders(self, start, end, dict):
        self.dict = dict
        self.indices = self.buildIndices(len(start), dict)

        self.bfs(end)
        self.res = []
        if start in self.distance:
            self.dfs(start, end, [start])

        return self.res




s = Solution()
start = "hit"
end = "cog"
dictionary = set(["hot","dot","dog","lot","log"])
print(s.buildIndices(3, dictionary))

print(s.findLadders(start, end, dictionary))


