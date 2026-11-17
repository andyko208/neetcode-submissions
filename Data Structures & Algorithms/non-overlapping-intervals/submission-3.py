class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time: O(n log n) from sorting
        # Space: O(n)
        n = len(intervals)
        # edge case to return 0 for a single interval
        if n == 1:
            return 0
        # sort the intervals
        intervals.sort()
        removals = 0
        start, end = intervals[0]
        # iterate through the list
        for curStart, curEnd in intervals[1:]:
            # find the overlap and greedily remove the longer interval(bigger end)
            if end > curStart:
                removals += 1
                end = min(end, curEnd)
            # no overlap, move onto the next
            else:
                end = curEnd
        # return the count
        return removals