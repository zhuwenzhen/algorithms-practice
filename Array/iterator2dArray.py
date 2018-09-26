'''
Given a 2d array, list of lists, write an iterator to iterate the 2d array

next(): Returns the next value in the array
has_next(): Returns T/F whether there is a nest value to return

2dArray = [
[1,2,3],
[4],
[5]
]

1
2
3
4
5

while has_next():
    print next()

'''


class MySolution(object):

    def __init__(self, twodarray):
        self.twodarray = twodarray
        self.len = len(twodarray)
        self.count = 0

    def has_next(self):
        if not self.twodarray or self.twodarray is None:
            return False
        return self.count < self.len

    def next(self):
        if self.has_next():
            currArr = self.twodarray[self.count]
            if currArr:
                return self.twodarray[self.count].pop(0)
            else:
                self.count += 1
                return self.next()
        else:
            raise StopIteration

arr = [
    [1, 2, 3],
    [4],
    [5]
]

s = MySolution(arr)
while s.has_next():
    print(s.next())
