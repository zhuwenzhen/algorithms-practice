"""
167. Add Two Numbers
You have two numbers represented by a linked list,
where each node contains a single digit.
The digits are stored in reverse order,
such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

Example
Given 7->1->6 + 5->9->2. That is, 617 + 295.

Return 2->1->9. That is 912.

Given 3->1->5 and 5->9->2, return 8->0->8.
"""

"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        head = ListNode(0)
        dummy = head
        carry = 0
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            dummy.val = carry % 10
            carry //= 10

            # if l1 and l2 haven't been completely visited
            # create a new node to store answer,
            # otherwise break the loop
            if l1 != None or l2 != None or carry != 0:
                dummy.next = ListNode(0)
                dummy = dummy.next
            else:
                break
        return head