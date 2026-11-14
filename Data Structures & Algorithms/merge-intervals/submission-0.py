class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time: O(n log n) from sorting
        # Space: O(n)

        # define variables
        n = len(intervals)
        # sort intervals by starting position
        intervals.sort()
        start, end = intervals[0]
        mergedIntervals = []
        # iterate through intervals from 1 to n
        for curStart, curEnd in intervals[1:]:
            # check for overlaps
            if end >= curStart:
                end = max(end, curEnd)
            # if no overlap, append to list
            else:
                mergedIntervals.append([start, end])
                # update the pointesr
                start, end = curStart, curEnd
        # additional append to make sure the last interval gets added
        mergedIntervals.append([start, end])
        
        return mergedIntervals