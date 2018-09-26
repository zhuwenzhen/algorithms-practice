"""
1443. Longest AB Substring
Given a string s of only 'A' and 'B', find the longest substring that satisfies the number of 'A' and 'B' are the same. Please output the length of this substring.

Example
Given s = "ABAAABBBA", return 8.

Explanation:
Substring s[0,7] and s[1,8] meet the conditions, their length is 8.
Given s = "AAAAAA", return 0.

Explanation:
No substring satisfies the condition except empty substring.
"""

import collections

class Solution:
    """
    @param S: a String consists of a and b
    @return: the longest of the longest string that meets the condition
    """
    #
    # def getAns(self, S):
    #     s = list(S)
    #     freq_table = collections.Counter(s)
    #
    #     if len(freq_table.values()) != 2:
    #         return 0
    #
    #     print(freq_table.values())
    #
    #     longest = 0
    #     for i in range(0, len(s) -1, 1):
    #         count = 0
    #         for j in range(i, len(s)-1, 2):
    #             if s[j] != s[j+1] :
    #                 count += 1
    #             else: count = 0
    #             print(s[j], s[j+1], count)
    #             if longest < count:
    #                 longest = count
    #     return longest * 2

    def getANs(self, word):
        length = 0
        cumulative_difference = 0
        first_index = {0: -1}
        for index, letter in enumerate(word):
            if letter == 'A':
                cumulative_difference += 1
            elif letter == 'B':
                cumulative_difference -= 1
            else:
                raise ValueError(letter)
            if cumulative_difference in first_index:
                length = max(length, index - first_index[cumulative_difference])
            else:
                first_index[cumulative_difference] = index
        return length

    def getAns(self, s):
        ans = 0

        if not s:
            return ans

        cnt_to_idx = {0: -1}
        cnt = 0

        for i in range(len(s)):
            if s[i] == 'A':
                cnt += 1
            else:
                cnt -= 1

            if cnt in cnt_to_idx:
                ans = max(ans, i - cnt_to_idx[cnt])
            else:
                cnt_to_idx[cnt] = i

        return ans
def longest_balanced(word):
    length = 0
    cumulative_difference = 0
    first_index = {0: -1}
    for index, letter in enumerate(word):
        if letter == 'A':
            cumulative_difference += 1
        elif letter == 'B':
            cumulative_difference -= 1
        else:
            raise ValueError(letter)
        if cumulative_difference in first_index:
            length = max(length, index - first_index[cumulative_difference])
        else:
            first_index[cumulative_difference] = index
    return length

s = Solution()
print(s.getAns("ABABABABABBBAABABB"))
print(longest_balanced("ABABABABABBBAABABB"))

