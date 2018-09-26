"""
471. Top K Frequent Words
Given a list of words and an integer k,
return the top k frequent words in the list.

Example
Given
[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]

for k = 3, return ["code", "lint", "baby"].

for k = 4, return ["code", "lint", "baby", "yes"],

Challenge
Do it in O(nlogk) time and O(n) extra space.
"""

import collections
import operator
import heapq

class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        wordsFreq = collections.OrderedDict()
        for w in words:
            if w in wordsFreq:
                wordsFreq[w] += 1
            else:
                wordsFreq[w] = 1

        print(wordsFreq)

        sortedFreq = (sorted(wordsFreq.items(), key = operator.itemgetter(1)))
        res = [t[0] for t in sortedFreq[-k::]]
        res.reverse()
        return res

    def topKFrequentWordsHeap(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        print(count.items())
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

s = Solution()
words = ["a","b","c","a","c"]
print(s.topKFrequentWords(words, 2))
print(s.topKFrequentWordsHeap(words, 2))


