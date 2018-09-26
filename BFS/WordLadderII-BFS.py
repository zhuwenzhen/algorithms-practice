"""
121. Word Ladder II
Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

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
    def findLadders(self, start, end, dict):
        # Write your code here
        dict.add(start)
        dict.add(end)

        def buildPath(path,word):
            if len(preMap[word]) == 0:
                result.append([word] + path)
                return
            path.insert(0,word)
            for w in preMap[word]:
                buildPath(path,w)
            path.pop(0)

        length = len(start)
        preMap = {}
        for word in dict:
            preMap[word] = []
        result = []
        cur_level = set()
        cur_level.add(start)

        while True:
            pre_level = cur_level
            cur_level = set()
            for word in pre_level:
                dict.remove(word)
            for word in pre_level:
                for i in range(length):
                    left = word[:i]
                    right = word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            nextWord = left + c + right
                            if nextWord in dict:
                                preMap[nextWord].append(word)
                                cur_level.add(nextWord)
            if len(cur_level) == 0:
                return []
            if end in cur_level:
                break
        buildPath([],end)
        return result