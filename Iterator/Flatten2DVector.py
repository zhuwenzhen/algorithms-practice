
"""
601. Flatten 2D Vector

Description
Implement an iterator to flatten a 2d vector.

Example
Given 2d vector =

[
  [1,2],
  [3],
  [4,5,6]
]
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,2,3,4,5,6].
"""

class Solution(object):

    # Initialize your data structure here
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.row = len(vec2d)
        self.i = 0

    def next(self):
        if self.hasNext():
            if self.vec2d[self.i]:
                return self.vec2d[self.i].pop(0)
            else:
                self.i += 1
                return self.next()

    def hasNext(self):
        return self.i < self.row



class CorrectSolution(object):
    def normalize(self):
        while (self.i != len(self.vec2d) and self.j == len(self.vec2d[self.i])):
            self.j = 0
            self.i += 1

    # Initialize your data structure here
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.i = 0
        self.j = 0
        self.normalize()

    def next(self):
        answer = None
        if (self.hasNext()):
            answer = self.vec2d[self.i][self.j]

        self.j += 1
        self.normalize()

        return answer

    def hasNext(self):
        return self.i != len(self.vec2d)


"""
def traverse(data):
    row = len(data)
    for i in range(row):
        vec = data[i]
        for j in range(len(vec)):
            print(data[i][j])
"""
"""
class Vector2D(object):
    def __init__(self, data):
        self.i, self.j = 0, 0
        self.data = data

    def next(self):
        self.j += 1
        return self.data[self.i][self.j-1]

    def hasNext(self):
        while self.i < len(self.data) and self.j >= len(self.data[self.i]):
            self.i += 1
            self.j = 0
        return self.i < len(self.data)
"""

test1 = [
  [],
  [1,2]
]

v = CorrectSolution(test1)
while v.hasNext():
    print(v.next())