class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Time: O(n log n) from sorting
        # Space: O(n) from sorting (tim sort)
        # count the number of drops for the interval
        # edge case
        if len(intervals) == 1:
            return 0
        # sort intervals
        intervals.sort()
        dropCount = 0
        _, prevEnd = intervals[0]
        # iterate through the intervals
        for curStart, curEnd in intervals[1:]:
            # found the overlap
            if prevEnd > curStart:
                dropCount += 1
                # update prevStart prevEnd
                prevEnd = min(prevEnd, curEnd)
            else:
                prevEnd = curEnd
        return dropCount

# edge cases
# [[1, 5], [2, 3]]