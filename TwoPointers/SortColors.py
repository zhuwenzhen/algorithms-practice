"""
148. Sort Colors
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Example
Given [1, 0, 1, 2], sort it in-place to [0, 1, 1, 2].

Challenge
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

"""
解法分析

在颜色排序（Sort Color）这个问题中，传统的双指针算法可以这么做：

1. 先用 partition 的方式区分开 0 和 1, 2
2. 再在右半部分区分开 1 和 2
3. 这个算法不可避免的要使用两次 Partition，
4. 写两个循环。许多面试官会要求你，能否只 partition 一次，也就是只用一个循环。

pl 和 pr 是传统的双指针，
分别代表 0~pl-1 都已经是 0 了，
pr+1~a.length - 1 都已经是 2 了。
另一个角度说就是，如果你发现了一个 0 ，
就可以和 pl 上的数交换，pl 就可以 ++；
如果你发现了一个 2 就可以和 pr 上的数交换 pr 就可以 --。
这样，我们用第三根指针 i 来循环整个数组。
如果发现 0，就丢到左边（和 pl 交换，pl++），如果发现 2，就丢到右边（和 pr 交换，pr--），
如果发现 1，就不管（i++）
这就是三根指针的算法，两根指针在两边，一根指针扫描所有的数。
这里有一个实现上的小细节，
当发现一个 0 丢到左边的时候，i需要++，
但是发现一个2 丢到右边的时候，i不用++。
原因是，从pr 换过来的数有可能是0或者2，需要继续判断丢到左边还是右边。
而从 pl 换过来的数，要么是0要么是1，不需要再往右边丢了。
因此这里 i 指针还有一个角度可以理解为，i指针的左侧，都是0和1。

类似的题
G家问过一个类似的题：给出 low, high 和一个数组，将数组分为三个部分，
< low, >= low & <= high, > high

解法和本题一模一样

"""
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        if nums is None or len(nums) <= 1:
            return nums

        left = 0
        right = len(nums) - 1

        i = 0
        while i <= right:
            if nums[i] == 0:  # swap with left
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 1:  # don't move
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1

        return nums