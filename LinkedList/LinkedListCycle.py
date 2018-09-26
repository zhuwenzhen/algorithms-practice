"""
102. Linked List Cycle
Given a linked list, determine if it has a cycle in it.

Example
Given -21->10->4->5, tail connects to node index 1, return true

Challenge
Follow up:
Can you solve it without using extra space?
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        if head is None:
            return False
        fast = head
        slow = head
        while True:
            if fast.next is not None:
                fast = fast.next.next
                slow = slow.next
                if fast is None or slow is None:
                    return False
                elif fast == slow:
                    return True
            else:
                return False
        return False