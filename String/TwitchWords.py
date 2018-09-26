"""
1401. Twitch Words
Our normal words do not have more than two consecutive letters.
If there are three or more consecutive letters, this is a tics.
Now give a word, from left to right,
to find out the starting point and ending point of all tics.

Example
Given str = "whaaaaatttsup", return [[2,6],[7,9]].

Explanation:
"aaaa" and "ttt" are twitching letters,
and output their starting and ending points.
Given str = "whooooisssbesssst",
return [[2,5],[7,9],[12,15]].

Explanation:
"ooo", "sss" and "ssss" are twitching letters,
and output their starting and ending points.
"""

class Solution:
    def twitchWords(self, str):
        n = len(str)
        res = []
        left, right = 0, 0
        for i in range(n):
            print(i)
            # two pointers
            while left < n and right < n and str[right] == str[left]:
                right += 1
            if right - left >= 3:
                res.append([left, right - 1])
            left = right
        return res

s = Solution()

test = "whaaaaatttsup"
print(s.twitchWords(test))