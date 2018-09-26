"""
938. Joseph Problem
n people are in a circle in order(numbered from 1 ~ n).
Start counting from 1 from the first person,
and the person who reports k goes out of the circle.
The next individual starts counting from 1 again and the person who reports k goes out of the circle.
Repeat this process until there are only 1 people in the circle,
which is the Joseph Problem.
Given n and k, find the last people's number.

Example
Given n = 5, k = 3, return 4.
Explanation:
Original Queue ：1 2 3 4 5
Round 1： 1 2 4 5, 3 goes out of the circle
Round 2： 2 4 5, 1 goes out of the circle
Round 3： 2 4, 5 goes out of the circle
Round 4： 4, 2 goes out of the circle
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: the last person's number
    """
    def josephProblem(self, n, k):

        # Make a cycle linked list
        dummy = ListNode(-1)
        curr = dummy
        for i in range(1, n + 1):
            curr.next = ListNode(i)
            curr = curr.next
        curr.next = dummy.next

        count = n
        prev = curr
        curr = dummy.next

        print("start", curr.val)

        while count > 1:
            person = (k - 1) % count + 1
            print("curr", curr.val)
            while person > 1:
                # kick out person out of cycle
                prev = curr
                curr = curr.next
                person -= 1
            prev.next = curr.next
            curr = curr.next
            count -= 1

        return curr.val

s = Solution()

print(s.josephProblem(5, 3))