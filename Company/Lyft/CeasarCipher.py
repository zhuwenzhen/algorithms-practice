"""
Ceasar Cipher
example:
abc + 2 --> cde, xyz + 2 --> zab
"""
class Solution:
    def cipher(self, s, shift):
        letterCount = 26
        res = ''

        for i in range(len(s)):
            ascii = (ord(s[i]) - ord('a') + shift + letterCount) % letterCount + ord('a')
            char = chr(ascii)
            res += char
        return res

s = Solution()
input = 'abc'
print(s.cipher(input, 3))