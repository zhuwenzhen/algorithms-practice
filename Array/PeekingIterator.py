# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.peekVal = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peekVal:
            return self.peekVal
        else:
            self.peekVal = self.it.next()
            return self.peekVal

    def next(self):
        """
        :rtype: int
        """
        if self.peekVal:
            res = self.peekVal
            self.peekVal = None
            return res
        else:
            return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.peekVal) or self.it.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    iter.next()         # Should return the same value as [val].