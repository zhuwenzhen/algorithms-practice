"""
914. Flip Game
You are playing the following Flip Game with your friend:
Given a string that contains only these two characters: + and -,
you and your friend take turns to flip two consecutive "++" into "--".
The game ends when a person can no longer make a move
and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example
Given s = "++++", after one move,
it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].
"""

class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        if s is None or not s:
            return []
        n = len(s)
        state = list(s)
        res = []
        for i in range(n-1):
            if state[i:i + 2] == ["+", "+"] :
                state[i:i + 2] = ["-","-"]
                res.append(''.join(state))
            state = list(s)
        return res

    def generatePossibleNextMoves1(self, s):
        ret = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if s[i]=="+":
                    ret.append(s[:i]+"--"+s[i+2:])
        return ret

s = Solution()
test = "+----+-++-++--+++-+--+----+-+-+-+++--+++"
print(s.generatePossibleNextMoves(test))