"""
104. Merge K Sorted Lists
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example
Given lists:
[
  2->4->null,
  null,
  -1->null
],
return -1->2->4->null.
"""
"""
Definition of ListNode

"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return other.val < self.val

import heapq

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return None

        dummy = ListNode(-1)
        curr = dummy
        heap = []
        for ll in lists:
            while ll:
                heapq.heappush(heap, ll.val)
                ll = ll.next

        while heap:
            # smallest
            node = ListNode(heapq.heappop(heap))
            curr.next = node
            curr = curr.next
        return dummy.next

a = ListNode(-1)
b = ListNode(5)
c = ListNode(11)
d = ListNode(6)
e = ListNode(10)

a.next = b
b.next = c

d.next = e

s = Solution()

res = s.mergeKLists([a, d])

if res:
    print(res.val, res.next.val)