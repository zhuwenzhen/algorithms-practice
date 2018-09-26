"""
120. Word Ladder
Given two words (start and end), and a dictionary,
find the length of shortest transformation sequence from start to end, such that:
Only one letter can be changed at a time
Each intermediate word must exist in the dictionary

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
"""
import collections
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        wordLen = len(start)
        queue = collections.deque([(start, 1)])

        while queue: # BFS
            curr = queue.popleft() # we want the head of the queue O(1)
            (currWord, currLen) = curr
            if currWord == end: return currLen
            for i in range(wordLen):
                part1, part2 = currWord[:i], currWord[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currWord[i] != j:
                        nextWord = part1 + j + part2 # enumerate all possible next word
                        if nextWord in dict: # check with dictionary and add next word in queue
                            queue.append((nextWord, currLen + 1)) # BFS
                            dict.remove(nextWord)

        return 0