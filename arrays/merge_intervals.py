"""Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '%s - %s' % (self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        if len(intervals) < 2:
            return intervals

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        result = [sorted_intervals[0]]
        for i in xrange(1, len(sorted_intervals)):
            prev = result[-1]
            curr = sorted_intervals[i]
            if prev.end >= curr.start:
                result[-1] = Interval(prev.start, max(curr.end, prev.end))
            else:
                result.append(curr)
        return result

if __name__ == '__main__':
    i1 = Interval(1, 4)
    i2 = Interval(2, 3)
    i3 = Interval(8, 10)
    i4 = Interval(15, 18)

    for interval in Solution().merge([i2, i1]):
        print interval
