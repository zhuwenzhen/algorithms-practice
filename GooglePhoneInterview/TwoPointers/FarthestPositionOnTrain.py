"""
Suppose you are on a long train,
you want to sit in a place which are farthest to everyone possible.
1 represents it's occupied, and 0 indicates it's empty.

input: [1,0,0,0,1]
output: 2

input: [1,0,0,0,0,1,0,1]
output: 2
"""

class Solution:

    # 先从左到右把数组扫一遍，记录每个0点左边最近的1，存到left[]
    # 从右到左再扫一遍，记录每个0点右边最近的1，存到right[]。
    # 最后对于每个位置为i的0号点，distance[i] = min(left[i],right[i])。

    def farthestSeat1(self, A):
        n = len(A)
        ppl_pos = []
        for i in range(n):
            if A[i] == 1:
                ppl_pos.append(i)

        left, right = [0 for _ in range(n)], [0 for _ in range(n)]
        distance = [0 for _ in range(n)]
        for i in range(n):
            if A[i] == 0:
                left[i] = min([i - j for j in ppl_pos if j < i])
                right[i]= min([j - i for j in ppl_pos if j > i])
                distance[i] = min(left[i], right[i])

        longest_distance = max(distance)
        return distance.index(longest_distance)

    def farthestSeat2(self, B):
        pass


s = Solution()
print(s.farthestSeat1([1,0,0,0,1]))



