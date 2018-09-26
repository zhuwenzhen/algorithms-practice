"""
473. Add and Search Word - Data structure design
Design a data structure that supports the following two operations: addWord(word) and search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or ..

A . means it can represent any one letter.

Example
addWord("bad")
addWord("dad")
addWord("mad")
search("pad")  // return false
search("bad")  // return true
search(".ad")  // return true
search("b..")  // return true
"""

class WordDictionary:
    def __init__(self):
        self.words = dict()
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        # write your code here
        if len(word) not in self.words:
            self.words[len(word)] = []
        self.words[len(word)].append(word)
    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        if len(word) not in self.words:
            return False
        else:
            for w in self.words[len(word)]:
                if self.check(w, word):
                    return True
            return False
    def check(self, exist_word, search_word):
        for i in range(0, len(exist_word)):
            if exist_word[i] != search_word[i] and search_word[i] != ".":
                return False
        return True