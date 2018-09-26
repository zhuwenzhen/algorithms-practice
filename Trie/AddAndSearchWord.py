"""
473. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:
addWord(word) and search(word)
search(word) can search a literal word or a regular expression
string containing only letters a-z or .. A . means it can represent any one letter.

Example
addWord("bad")
addWord("dad")
addWord("mad")
search("pad")  // return false
search("bad")  // return true
search(".ad")  // return true
search("b..")  // return true
"""
class Solution:
    def exist(self, board, word):
        if word == []:
            return True
        m, n = len(board), len(board[0])
        if m == 0 or n == 0: return False
        visited = [[False for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, visited, i, j):
                    return True
        return False

    def dfs(self, board, word, visited, row, col):
        if word == '':
            return True
        m, n = len(board), len(board[0])

        if row < 0 or row >= m or col < 0 or col >= n:
            return False

        if board[row][col] == word[0] and not visited[row][col]:
            visited[row][col] = True
            if self.dfs(board, word[1:], visited, row - 1, col) or \
                    self.dfs(board, word[1:], visited, row, col - 1) or \
                    self.dfs(board, word[1:], visited, row + 1, col) or \
                    self.dfs(board, word[1:], visited, row, col + 1):
                return True
            else:
                visited[row][col] = False
        return False

s = Solution()
