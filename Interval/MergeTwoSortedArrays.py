"""
6. Merge Two Sorted Arrays
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
"""


class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        if not A:
            return B

        if not B:
            return A

        idxA, idxB, result = 0, 0, []
        while idxA < len(A) and idxB < len(B):
            if A[idxA] < B[idxB]:
                result.append(A[idxA])
                idxA += 1
            else:
                result.append(B[idxB])
                idxB += 1

        if idxA < len(A):
            for i in range(idxA, len(A)):
                result.append(A[i])

        if idxB < len(B):
            for i in range(idxB, len(B)):
                result.append(B[i])

        return result