class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # drop the interval that ends later
        # count the number of drops for the interval that is to the left of the current
        # edge case
        if len(intervals) == 1:
            return 0
        # sort intervals
        intervals.sort()
        dropCount = 0
        prevStart, prevEnd = intervals[0]
        for curStart, curEnd in intervals[1:]:
            # found the overlap
            if prevEnd > curStart:
                dropCount += 1
                # update prevStart prevEnd
                prevEnd = min(prevEnd, curEnd)
            else:
                prevEnd = curEnd
        return dropCount
