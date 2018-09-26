"""
public class Solution {
    /**
     * @param arr: The array you should handle
     * @return: Return the product
     */
    public int[] getProduct(int[] arr) {
        // Write your code here
        if(arr.length == 1) {
            int[] ans = new int[1];
            ans[0] = 0;
            return ans;
        }
        int[] pre = new int[arr.length];
        int[] suf = new int[arr.length];
        int[] ans = new int [arr.length];
        pre[0] = arr[0];
        for(int i = 1; i < arr.length; i++) {
            pre[i] = arr[i] * pre[i - 1];
        }
        suf[arr.length - 1] = arr[arr.length - 1];
        for(int i = arr.length - 2; i >= 0; i--) {
            suf[i] = suf[i + 1] * arr[i];
        }
        ans[0] = suf[1];
        ans[arr.length - 1] = pre[arr.length - 2];
        for(int i = 1; i <= arr.length - 2; i++) {
            ans[i] = pre[i - 1] * suf[i + 1];
        }
        return ans;
    }
}

题目描述
输入为整数数组 arr，请你返回结果数组 ans，使得 ans[i] 为 arr 中除了 arr[i] 以外的所有数的乘积。

"""

"""
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal 
to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? 
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 1:
            res = [0]
            return res

        n = len(nums)
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]
        res = [0 for _ in range(n)]
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]

        suffix[n - 1] = nums[n - 1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]

        res[0] = suffix[1]
        res[n-1] = prefix[n-2]

        for i in range(1, n-1):
            res[i] = prefix[i - 1] * suffix[i + 1]

        return res

A = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(A))