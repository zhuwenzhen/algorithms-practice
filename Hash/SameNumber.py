"""
1368. Same Number
Given an array, If the same number exists in the array,
and the distance of the same number is less than the given value k,
output YES, otherwise output NO.

Example
Given array = [1,2,3,1,5,9,3], k = 4, return "YES".

Explanation:
The distance of 1 whose indexes are 3 and 0 is 3,
which meets the requirement and output YES.
Given array = [1,2,3,5,7,1,5,1,3], k = 4, return "YES".

Explanation:
The distance of 1 whose indexes are  7 and 5 is 2,
which meets the requirement and output YES.
"""
class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        hash = {}
        n = len(nums)

        for a in nums:
            hash[a] = []

        for i in range(n):
            hash[nums[i]].append(i)

        for _, freq in hash.items():
            if len(freq) >= 2:
                for i in range(0, len(freq) - 1):
                    if (freq[i + 1] - freq[i]) < k:
                        return "YES"
        return "NO"

s = Solution()
array = [1, 2, 3, 1, 5, 9, 3]
k = 4
print(s.sameNumber(array, 4))