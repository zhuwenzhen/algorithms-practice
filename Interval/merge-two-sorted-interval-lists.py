"""
839. Merge Two Sorted Interval Lists
Merge two sorted (ascending) lists of interval and return it as a new sorted list.
The new sorted list should be made by splicing together the intervals
of the two lists and sorted in ascending order.

Example
Given list1 = [(1,2),(3,4)] and list2 = [(2,3),(5,6)],
return [(1,4),(5,6)].
"""
"""
正如课上说的，
用一个 last 来记录最后一个还没有被放到 merge results 里的 Interval，
用于和新加入的 interval 比较看看能不能合并到一起。
时间复杂度 O(n+m)
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

    def mergeTwoInterval(self, list1, list2):
        res = []
        if list1 is None or not list1: return res
        if list2 is None or not list2: return res

        last = Interval(0, 0)
        curr = Interval(0, 0)

        i, j = 0, 0

        len1 = len(list1)
        len2 = len(list2)

        res = []

        while i < len1 and j < len2:
            if list1[i].start < list2[j].start:
                curr = list1[i]
                i += 1
            else:
                curr = list2[j]
                j += 1

            last = self.merge(res, last, curr)

        while i < len1:
            last = self.merge(res, last, list1[i])
            i += 1

        while j < len2:
            last = self.merge(res, last, list2[j])
            j += 1

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

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        res = []
        if list1 is None or not list1: return res
        if list2 is None or not list2: return res

        return res

    def merge(self, res, last, curr):
        if last is None:
            return curr

        if curr.start > last.end:
            res.append(last)
            return curr

        last.end = max(last.end, curr.end)
        return last


class Solution2:

    def checkOverlapped(self, intv_1, intv_2):

        if intv_1.end < intv_2.start:  # not overlap
            return False, None
        else:
            right_boundary = max(intv_1.end, intv_2.end)
            return True, Interval(intv_1.start, right_boundary)

    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):

        if list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif not list1 and not list2:
            return []

        iter_1, iter_2 = 0, 0
        result = []
        while iter_1 < len(list1) and iter_2 < len(list2):
            intv_1 = list1[iter_1]
            intv_2 = list2[iter_2]

            if intv_1.start < intv_2.start:
                result += [intv_1]
                iter_1 += 1
            else:
                result += [intv_2]
                iter_2 += 1
        while iter_1 < len(list1):
            result += [list1[iter_1]];
            iter_1 += 1
        while iter_2 < len(list2):
            result += [list2[iter_2]];
            iter_2 += 1

        result_2 = [result[0]]
        # i = 0
        for i in range(1, len(result)):
            check, merge = self.checkOverlapped(result_2[-1], result[i])

            if not check:
                result_2 += [result[i]]
            else:
                result_2[-1] = merge

        return result_2

# TEST
list1 = [Interval(1,2), Interval(3, 4)]
list2 = [Interval(2,3), Interval(5, 6)]
s = Solution2()
res = s.mergeTwoInterval(list1, list2)
for i in res:
    print(i.start, i.end)