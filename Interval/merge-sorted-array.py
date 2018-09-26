"""
64. Merge Sorted Array
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]
"""

"""
因为AB 都是升序数组，所以在merge时候可以从大的一端 或者 小的一端进行merge
此题从后向前merge， 判断出界条件是其中一个数组的index < 0
需要创造一个新数组来存放merge后的结果，长度为 A.len + B.len

I think in the real interview 
the interviewer won't give you an array A with some empty slots and merge it on A. 
It's stupid and not intuitive.
So just merge two sorted array without giving m, n, 
I shall create a new array: merge = [] to store the merged result.
"""

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        i = m - 1
        j = n - 1
        index = m + n - 1

        merged = [0 for _ in range(m + n)]

        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                merged[index] = A[i]
                index -= 1
                i -= 1
            else:
                merged[index] = B[j]
                index -= 1
                j -= 1

        while i >= 0:
            merged[index] = A[i]
            index -= 1
            i -= 1

        while j >= 0:
            merged[index] = B[j]
            index -= 1
            j -= 1

        return merged

    def mergeSortedArray(self, A, B):
        m = len(A)
        n = len(B)
        merged = [0 for _ in range(m + n)]

        i = m - 1
        j = n - 1
        index = m + n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                merged[index] = A[i]
                index -= 1
                i -= 1
            else:
                merged[index] = B[j]
                index -= 1
                j -= 1

        while i >= 0:
            merged[index] = A[i]
            index -= 1
            i -= 1

        while j >= 0:
            merged[index] = B[j]
            index -= 1
            j -= 1

        return merged



s = Solution()
A = [1, 2, 3]
B = [4, 5]
print(s.mergeSortedArray(A, 3, B, 2))