"""
575. Decode String
Given an expression s includes numbers, letters and brackets. Number represents the number of repetitions inside the brackets(can be a string or another expression)．Please expand expression to be a string.

Example
s = abc3[a] return abcaaa
s = 3[abc] return abcabcabc
s = 4[ac]dy, return acacacacdy
s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz

Challenge
Can you do it without recursion?
"""


def expressionExpand(self, s):
    # write your code here
    return self.helper(s)


# this returns a string
def helper(self, s):
    ans = ""
    num = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num += s[i]
            i += 1
        elif s[i] == "[":
            index = self.find_matching_paren(s, i)
            substring = s[i + 1:index]
            ans += int(num) * self.helper(substring)
            i = index + 1
            num = ""
        else:  # s[i] is normal letter
            ans += s[i]
            i += 1
    return ans


def find_matching_paren(self, s, index):
    count = 0
    for i in range(index, len(s)):
        if s[i] == '[':
            count += 1
        elif s[i] == ']':
            count -= 1
        if count == 0:
            return i
    return index