"""
990. Beautiful Arrangement

Suppose you have N integers from 1 to N.
We define a beautiful arrangement as an array
that is constructed by these N numbers successfully
if one of the following is true for the ith position
(1 <= i <= N) in this array:
The number at the ith position is divisible by i.
i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?
Example
Input: 2
Output: 2
Explanation:
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
"""
import collections
class Solution:
    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    count = 0
    def countArrangement(self, N):
        if N == 0: return 0
        nums = [i for i in range(N+1)]
        self.helper(nums, N)
        return self.count

    def helper(self, nums, start):
        if start == 0:
            self.count += 1
            return

        for i in range(start, 0, -1):
            print(start, nums[i])
            nums[start], nums[i] = nums[i], nums[start]
            if nums[start] % start == 0 or start % nums[start] == 0:
                self.helper(nums, start - 1)
            nums[start], nums[i] = nums[i], nums[start]

    def countArrangement2(self, N):
        # Write your code here
        dp = collections.defaultdict()

        def dfs(index, nums):
            if len(nums) == 0:
                return 1
            key = tuple(nums)
            if key in dp:
                return dp[key]
            ans = 0
            for i, n in enumerate(nums):
                if n % index == 0 or index % n == 0:
                    nexts = nums[:i] + nums[i + 1:]
                    ans += dfs(index + 1, nexts)
            dp[key] = ans
            return ans
        return dfs(1, range(1, N + 1))
"""
"""

s = Solution()
print(s.countArrangement(4))



