class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    # Version 1: Classical Binary Search
    def findPosition(self, A, target):
        if A is None or len(A) == 0 or target is None:
            return -1

        start, end = 0, len(A) - 1
        # Key 1: start + 1 < end
        while start + 1 < end:
            # Key 2:start + (end - start) / 2
            mid = start + (end - start) // 2
            # Key 3:Cases =, <, >, mid not + 1 or -1
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid

        # Key 4: After while loop, separately do start and end
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


    # Version 2: Recursion
    def findPosition2(self, A, target):
        return self.binarySearch(A, 0, len(A) - 1, target)

    def binarySearch(self, A, start, end, target):
        if start > end:
            return -1

        mid = start + (end - start) // 2

        if A[mid] == target:
            return mid
        elif A[mid] < target:
            return self.binarySearch(A, mid + 1, end, target)
        else:
            return self.binarySearch(A, start, mid - 1, target)


