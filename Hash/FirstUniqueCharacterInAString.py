"""
209. First Unique Character in a String
Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

Example
For "abaccdeff", return 'b'.
"""
import collections
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):

        str_list = list(str)
        frequency_table = collections.Counter(str_list)

        for word, freq in frequency_table.items():
            if freq == 1:
                return word
        return -1






