
"""
423. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Example
The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        if s is None or not s or len(s) % 2 == 1:
            return False

        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif not stack:
                return False
            else:
                r = stack.pop()
                if r == '(' and c != ')':
                    return False
                if r == '[' and c != ']':
                    return False
                if r == '{' and c != '}':
                    return False
        return not stack