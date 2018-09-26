"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
a move consists of either replacing one occurrence of "XL" with "LX",
or replacing one occurrence of "RX" with "XR".
Given the starting string start and the ending string end,
return True if and only if there exists a sequence of moves to
transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Note:

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""

class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if start.replace('X','')!=end.replace('X',''): return False

        l1=l2=r1=r2=0
        for v1,v2 in zip(start,end):
            if v1=='L': l1+=1
            elif v1=='R': r1+=1
            if v2=='L': l2+=1
            elif v2=='R': r2+=1
            if l1>l2 or r1<r2: return False
        return True


    """
    This is actually a good quesion. Why does everybody donw vote it. 
    We can imagine R as the walker who can only walk right, 
    and L as the walker who can only walk left. 
    X is the empty space that walkers can pass through
"""
# class Solution {
#     public boolean canTransform(String start, String end) {
#         int i = 0, j = 0;
#         if(start.length() != end.length()) return false;
#         while(i < start.length() && j < end.length()){
#             while(i < start.length() && start.charAt(i) == 'X') ++i;
#             while(j < end.length() && end.charAt(j) == 'X') ++j;
#             if(i == start.length() || j == end.length()) break;
#             if(start.charAt(i) != end.charAt(j)) return false;
#             if(start.charAt(i) == 'R' && i > j) return false;
#             else if(start.charAt(i) == 'L' && i < j) return false;
#             ++i;
#             ++j;
#         }
#         while(i < start.length() && start.charAt(i) == 'X') ++i;
#         while(j < end.length() && end.charAt(j) == 'X') ++j;
#         return i == j;
#     }
# }

"""
follow up：
如果LR只能轮流走，R先走，直到有一方不能走

"""