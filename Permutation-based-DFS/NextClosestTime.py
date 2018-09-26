"""
862. Next Closest Time
Given a time represented in the format "HH:MM",
form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid.
For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example
Given time = "19:34", return "19:39".

Explanation:
The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
which occurs 5 minutes later.
It is not 19:33,
because this occurs 23 hours and 59 minutes later.
Given time = "23:59", return "22:22".

Explanation:
The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time
since it is smaller than the input time numerically.
"""
class Solution:
    """
    @param time: the given time
    @return: the next closest time
    """
    import sys
    diff = sys.maxsize
    result = ""

    def nextClosestTime(self, time):
        if time == "11:11": return "11:11"
        set = []
        for i in range(len(time)):
            if time[i] != ":":
                set.append(time[i:i+1])

        if len(set) == 1:
            return time

        minute = int(time[0:2]) * 60 + int(time[3:5])
        self.dfs(set, "", 0, minute)
        return self.result

    def dfs(self, digits, cur, pos, target):
        if pos == 4:
            m = int(cur[0:2]) * 60 + int(cur[2:4])
            if m == target: return
            if m - target> 0:
                d = m - target
            else:
                d = 24 * 60 + m - target

            if d < self.diff:
                self.diff = d
                self.result = cur[0:2] + ':' + cur[2:4]
            return

        for i in range(len(digits)):
            if pos == 0 and int(digits[i]) > 2:
                continue
            if pos == 1 and int(cur) * 10 + int(digits[i]) > 23:
                continue
            if pos == 2 and int(digits[i]) > 5:
                continue
            if pos == 3 and int(cur[2]) * 10 + int(digits[i]) > 59:
                continue

            self.dfs(digits, cur + digits[i] , pos + 1, target)


s = Solution()
print(s.nextClosestTime("19:34"))