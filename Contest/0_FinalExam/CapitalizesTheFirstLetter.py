"""
936. Capitalizes The First Letter
Given a sentence of English, update the first letter of each word to uppercase.

Example
Given s = "i want to get an accepted", return "I Want To Get An Accepted".
"""

class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        return s.title()
        # s = s.split(" ")
        # text = [word for word in s]
        # for w in text:
        #     w