"""
132. Word Search II
Given a matrix of lower alphabets and a dictionary.
Find all words in the dictionary that can be found in the matrix.
A word can start from any position in the matrix
and go left/right/up/down to the adjacent position.

Example

Given matrix:
doaf
agai
dcan

and dictionary:
{"dog", "dad", "dgdg", "can", "again"}
return {"dog", "dad", "can", "again"}

dog:
doaf
agai
dcan

dad:
doaf
agai
dcan

can:
doaf
agai
dcan

again:
doaf
agai
dcan


Challenge

Using trie to implement your algorithm.
"""

class Trie:
    def __init__(self):
        self.children = {}
        self.flag = False
        self.hasWord = False

    def put(self, key):
        if key == '':
            self.flag = True
            self.hasWord = True
            return
        if key[0] not in self.children:
            self.children[key[0]] = Trie()


