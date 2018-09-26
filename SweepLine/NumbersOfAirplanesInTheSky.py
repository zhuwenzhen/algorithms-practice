"""
391. Number of Airplanes in the Sky
Given an interval list which are flying and landing time of the flight.
How many airplanes are on the sky at most?

Example
For interval list

[
  (1,10),
  (2,3),
  (5,8),
  (4,7)
]

Return 3
"""

"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


import functools
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def comparator(self, event1, event2):
        if event1[0] != event2[0]:
            return event1[0] - event2[0]
        else:
            return event1[1] - event2[1]

    def countOfAirplanes(self, airplanes):
        events = []
        for airplane in airplanes:
            events.append((airplane.start, 1))
            events.append((airplane.end, -1))
        events = sorted(events, key = functools.cmp_to_key(self.comparator))

        count = 0
        most = 0

        for t, delta in events:
            count += delta
            most = max(most, count)

        return most

interval_list = [
  (1,10),
  (2,3),
  (5,8),
  (4,7)
]

intervals = []
for i in interval_list:
    intervals.append(Interval(i[0], i[1]))
print(intervals)
s = Solution()
res = s.countOfAirplanes(intervals)
print(res.start, res.end)
