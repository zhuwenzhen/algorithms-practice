


# https://www.lintcode.com/problem/add-bold-tag-in-string/leaderboard


class Solution:
    """
    @param s: a string
    @param dict: a list of strings
    @return: return a string
    """
    def addBoldTag(self, s, dict):
        # write your code here
        L = len(s)
        bold = [False for _ in range(L)]
        for i in range(L):
            end = i
            for j in range(i+1,L+1):
                if s[i:j] in dict:
                    end = j
            bold[i:end] = [True for _ in range(end-i)]
        bold = [False]+bold+[False]
        res = []
        for i in range(L):
            if bold[i+1] and not bold[i]:
                res.append("<b>")
            res.append(s[i])
            if bold[i+1] and not bold[i+2]:
                res.append("</b>")
        return "".join(res)




    def addBoldTag(self, s, dict):
        # # write your code here
        tag_loc = [0 for _ in range(len(s))]
        import re
        for item in dict:
            l = len(item)
            loc = [m.start() for m in re.finditer(item ,s)]
            if loc:
                for i in loc:
                    for idx in range(i , i +l):
                        tag_loc[idx] =1

        # compose return string
        prev = 0
        ret = ''
        for i, ch in enumerate(s):
            if prev == 0 and tag_loc[i] == 1:
                ret += '<b>' + ch
                prev = 1
            elif prev == 1 and tag_loc[i] == 0:
                ret += '</b>' + ch
                prev = 0
            else:
                ret += ch
        if tag_loc[-1] == 1:
            ret += '</b>'

        return ret