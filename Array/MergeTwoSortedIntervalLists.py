"""
839. Merge Two Sorted Interval Lists
Merge two sorted (ascending) lists of interval and return it as a new sorted list.
The new sorted list should be made by splicing together the intervals of the two lists and sorted in ascending order.

Example
Given list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)], return [(1,4),(5,6)].
"""


"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoIntervals(self, list1, list2):
        res = []
        if list1 is None or list2 is None:
            return res

        i, j = 0, 0
        last = None

        while i < len(list1) and j < len(list2):
            # pick the smaller one to be curr
            if list1[i].start < list2[j].start:
                curr = list1[i]
                i += 1
            else:
                curr = list2[j]
                j += 1
            # use last as a buffering container
            last = self.merge(res, last, curr)

        while i < len(list1):
            last = self.merge(res, last, list1[i])
            i += 1
        while j < len(list2):
            last = self.merge(res, last, list2[j])
            j += 1

        # Add buffering last in to result in the end
        if last is not None:
            res.append(last)
        return res

    def merge(self, res, last, curr):
        if last is None:
            return curr

        if curr.start > last.end:
            res.append(last)
            return curr

        last.end = max(last.end, curr.end)
        return last

list1 = [Interval(1, 2), Interval(3, 4)]
list2 = [Interval(2, 3), Interval(5, 6)]
s = Solution()
res = s.mergeTwoIntervals(list1, list2)
print(len(res))
for elem in res:
    print(elem.start, elem.end)