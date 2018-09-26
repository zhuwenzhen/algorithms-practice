"""
给定两个字符串，请设计一个方法来判定其中一个字符串是否为另一个字符串的置换。
置换的意思是，通过改变顺序可以使得两个字符串相等
"""

class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        A = sorted(A)
        B = sorted(B)
        return A == B