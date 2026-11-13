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
        intervalsList = [[interval.start, interval.end] for interval in intervals]
        # print(intervalsList)
        intervalsList.sort()
        # handle the edge case
        if len(intervalsList) <= 1:
            return True
        # keep the start, end = intervals[0]
        prevStart, prevEnd = intervalsList[0]
        # iterate through intervalsList 1 to n and check if next start is < prev end to return False
        for curStart, curEnd in intervalsList[1:]:
            if prevEnd > curStart:
                return False
            # update the pointers
            prevStart, prevEnd = curStart, curEnd
        return True
