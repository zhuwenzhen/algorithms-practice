"""
165. Merge Two Sorted Lists
Merge two sorted (ascending) linked lists and return it as a new sorted list.
The new sorted list should be made by splicing together
the nodes of the two lists and sorted in ascending order.

Example
Given 1->3->8->11->15->null, 2->null , return 1->2->3->8->11->15->null.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        # make a dummy node to hold the head
        dummy = ListNode(0)
        tmp = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 is not None:
            tmp.next = l1
        else:
            tmp.next = l2

        return dummy.next

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l8 = ListNode(8)
l11 = ListNode(11)
l15 = ListNode(15)

l1.next = l3
l3.next = l8
l8.next = l11
l2.next = l15

s = Solution()
merged = s.mergeTwoLists(l1, l2)

print(merged.val)
print(merged.next)
while merged:
    print(merged.val)
    merged = merged.next