"""
362. Sliding Window Maximum
Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from the start of the array, find the maximum number inside the window at each moving.

Example
For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

At first the window is at the start of the array like this

[|1, 2, 7| ,7, 8] , return the maximum 7;

then the window move one step forward.

[1, |2, 7 ,7|, 8], return the maximum 7;

then the window move one step forward again.

[1, 2, |7, 7, 8|], return the maximum 8;

Challenge
o(n) time and O(k) memory


"""

import collections
class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """

    def maxSlidingWindow(self, nums, k):
        q = collections.deque()
        res = []
        if len(nums) < k or k == 0:
            return []

        n = len(nums)
        for i in range(n):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if i < k - 1:
                continue

            while len(q) and q[0] <= i - k:
                q.popleft()

            res.append(nums[q[0]])

        return res


    def maxSlidingWindow2(self, nums, k):
        res = []
        if nums is None or not nums:
            return res

        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            res.append(max(window))

        return res
