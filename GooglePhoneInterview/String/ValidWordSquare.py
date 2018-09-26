"""
888. Valid Word Square
Given a sequence of words, check whether it forms a valid word square.
A sequence of words forms a valid word square if the k^th row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

Example
Given
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]
return true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".

Therefore, it is a valid word square.
Given
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]
return true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".

Therefore, it is a valid word square.
Given
[
  "ball",
  "area",
  "read",
  "lady"
]
return false

Explanation:
The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.
"""
class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # matrix = [list(w) for w in words]
        n = len(words)
        print(n)
        matrix = []

        for w in words:
            length = len(w)
            if length != n:
                w = w + 'i' * (n - length)
                matrix.append(list(w))
            else: matrix.append(list(w))

        transpose = list(map(list, zip(*matrix)))
        return transpose == matrix

    # Rank 1
    def validWordSquare1(self, words):
        # Write your code here
        check = True
        i= 1
        while i < len(words) and check:
            if words[0][i] != words[i][0]:
                check = False
            i += 1
        return  check

    # Rank 2:
    def validWordSquare2(self, words):
        # Write your code here
        for i in range(len(words)):
            for j in range(i,len(words[i])):
                if words[i][j] != words[j][i]:
                    return False
        return True

    # others
    def validWordSquareO(self, words):
        # Write your code here
        n = 0
        for word in words: n = max(n, len(word))
        for word in words:
            if len(word) < n: word += ' ' * (n - len(word))
        for i in range(len(words)):
            for j in range(n):
                if words[i][j] != words[j][i]: return False
        return True

s = Solution()
words = [
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

s.validWordSquare(words)
