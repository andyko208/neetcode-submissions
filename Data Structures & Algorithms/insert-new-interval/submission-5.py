class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Time: O(n) from iterating intervals
        # Space: O(n) for storing all intervals
        insertedIntervals = []
        mergeStart, mergeEnd = newInterval
        # append all intervals that ends earlier than newInterval
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < mergeStart:
            insertedIntervals.append(intervals[i])
            i += 1
        # merge all overlapping intervals and append it
        while i < n and mergeEnd >= intervals[i][0]:
            mergeStart = min(intervals[i][0], mergeStart)
            mergeEnd = max(intervals[i][1], mergeEnd)
            i += 1
        insertedIntervals.append([mergeStart, mergeEnd])
        # append all intervals that starts later than merged 
        while i < n:
            insertedIntervals.append(intervals[i])
            i += 1
        return insertedIntervals

# [[1, 4], [6, 7]], [2, 5]