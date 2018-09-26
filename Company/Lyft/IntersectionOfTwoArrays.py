"""
LintCode 547. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

Example
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Challenge
Can you implement it in three different algorithms?
"""

""" Method 1: HashTable"""
class HashTable:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hs = {}
        n1, n2 = len(nums1), len(nums2)
        for i in range(n1):
            if nums1[i] in hs:
                hs[nums1[i]] +=1
            else:
                hs[nums1[i]] = 1

        res = []
        for i in range(n2):
            if nums2[i] in hs and hs[nums2[i]] > 0:
                res.append(nums2[i])
                hs[nums2[i]] -= 1

        return list(set(res))

""" Method 2: Sort then Merge """
class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        index = 0
        n1, n2 = len(nums1), len(nums2)
        tmp = [0 for _ in range(n1)]

        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                if index == 0 or tmp[index - 1] != nums1[i]:
                    tmp[index] = nums1[i]
                    index += 1
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        res = [0 for _ in range(index)]
        for k in range(index):
            res[k] = tmp[k]
        return res

s = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(s.intersection(nums1, nums2))



