
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if not L or sum(L) <= k or k <= 0:
            return 0

        def count_piece(wood_length):
            num_pieces = 0
            for length in L:
                num_pieces += length // wood_length
            return num_pieces

        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) // 2
            num_pieces = count_piece(mid)
            if num_pieces >= k:
                start = mid
            else:
                end = mid
        if count_piece(end) >= k:
            return end
        if count_piece(start) >= k:
            return start
        return 0