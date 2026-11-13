"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Time: O(n log n) from sorting
        # Space: O(n)
        # sort intervalsList
        intervals.sort(key=lambda x: x.start)
        # handle the edge case
        if len(intervals) <= 1:
            return True
        # keep the start, end = intervals[0]
        prevEnd = intervals[0].end
        # iterate through intervalsList 1 to n and check if next start is < prev end to return False
        for interval in intervals[1:]:
            if prevEnd > interval.start:
                return False
            # update the pointers
            prevEnd = interval.end
        return True
