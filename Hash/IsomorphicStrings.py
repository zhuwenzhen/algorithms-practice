"""
方法一：首先遍历s，将字符串映射出整数存在数组中。
再遍历T，比较两个整数数组是不是值相同。

方法二：判断对应位置字符是否成唯一映射，同时判断是否出现重复映射。
"""

"""

加面，给一个secret字符串和一个test字符串，判断它们是否encoded（字母一一对应）。
follow-up问如果是millions of数据怎么办。

"""
class Solution:

    def isIsomorphic(self, s, t):
        # write your code here

        if len(s) != len(t):
            return False

        n = len(s)
        ms = [0 for _ in range(256)]
        mt = [0 for _ in range(256)]

        for i in range(n):
            if ms[ord(s[i])] != mt[ord(t[i])]:
                return False
            ms[ord(s[i])] = i
            mt[ord(t[i])] = i

        return True
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """
    def isIsomorphic(self, s, t):
        # write your code here
        # dic, vs = {},set()
        # for i,val in enumerate(s):
        #     vs.add(t[i])
        #     if val in dic:
        #         if dic[val] != t[i]:
        #             return False
        #     else:
        #         dic[val] = t[i]
        #     if len(vs) != len(dic):
        #         return False
        # return True
        dic, vs = {},{t[0]}
        for i,val in enumerate(s):
            vs.add(t[i])
            if val in dic:
                if dic[val] != t[i]:
                    return False
            else:
                dic[val] = t[i]
            if len(vs) != len(dic):
                return False
        return True
"""

https://www.lintcode.com/problem/isomorphic-strings/description

public class Solution {
    /**
     * @param s a string
     * @param t a string
     * @return true if the characters in s can be replaced to get t or false
     */
    public boolean isIsomorphic(String s, String t) {
        // Write your code here
        int[] map = new int[256];  // ASCII 的范围是0-255
        char[] sc = s.toCharArray();
        char[] tc = t.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            if (map[sc[i]] == 0) {
                map[sc[i]] = tc[i];
            } else {
                if (map[sc[i]] != tc[i]) {
                    return false;
                }
            }
        }

        int[] map2 = new int[256];
        for (int i = 0; i < t.length(); i++) {
            if (map2[tc[i]] == 0) {
                map2[tc[i]] = sc[i];
            } else {
                if (map2[tc[i]] != sc[i]) {
                    return false;
                }
            }
        }

        return true;
    }
}
"""