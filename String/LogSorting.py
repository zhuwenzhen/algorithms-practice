"""
1380. Log Sorting
Give a log, consisting of List< String >,
each element representing one line of logs.
Each line of log information is separated by a space.
The first is the ID of the log,
followed by the log content.

There are two ways to make content:

All consist of letters and spaces.
All consist of numbers and spaces.
Now that the logs are sorted,
it is required that component 1 be sorted in order of content lexicography
 and placed at the top, and component 2 should be placed at the bottom and output in the order of input. (Note that the space also belongs to the content, and when the lexicographic order of the composition method 1 is equal, sort according to the dictionary order of log ID., and the guarantee ID is not repeated)
Example
Given

[
    "zo4 4 7",
    "a100 Act zoo",
    "a1 9 2 3 1",
    "g9 act car"
]
, return

[
    "a100 Act zoo",
    "g9 act car",
    "zo4 4 7",
    "a1 9 2 3 1"
]

Explanation:
"Act zoo" < "act car", So the output is as above.
Given
[
    "zo4 4 7",
    "a100 Actzoo",
    "a100 Act zoo",
    "Tac Bctzoo",
    "Tab Bctzoo",
    "g9 act car"
]
, return

[
    "a100 Act zoo",
    "a100 Actzoo",
    "Tab Bctzoo",
    "Tac Bctzoo",
    "g9 act car",
    "zo4 4 7"
]
Explanation:
Because "Bctzoo" == "Bctzoo", the comparison "Tab" and "Tac" have "Tab" < Tac ", so" Tab Bctzoo "< Tac Bctzoo".
Because ' '<'z', so "A100 Act zoo" < A100 Actzoo".
"""
import functools
class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """

    def cmpFunction(self, a, b):
        index1 = a.find(" ")
        id_a = a[:index1]
        content_a = a[index1+1:]
        index2 = b.find(" ")
        id_b = b[:index2]
        content_b = b[index2+1:]

        if content_a != content_b:
            if content_a < content_b:
                return -1
            else:
                return 1
        if id_a < id_b:
            return -1
        else:
            return 1

    def logSort(self, logs):
        sorted_logs = sorted(logs, key = functools.cmp_to_key(self.cmpFunction))
        print(logs)
        print(sorted_logs)
        res = []
        for log in sorted_logs:
            index = log.find(" ")
            if log[index + 1].isalpha():
                res.append(log)
        for log in logs:
            index = log.find(" ")
            if not log[index + 1].isalpha():
                res.append(log)
        return res


s = Solution()
logs = [
    "zo4 4 7",
    "a100 Actzoo",
    "a100 Act zoo",
    "Tac Bctzoo",
    "Tab Bctzoo",
    "g9 act car"
]
print(s.logSort(logs))