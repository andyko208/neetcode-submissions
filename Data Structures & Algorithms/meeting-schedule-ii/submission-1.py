"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # create a min heap to store the end of the intervals and pop if start is bigger
        # Time: O(n) from iterating through the intervals
        # Space: O(n) from storing the entire intervals in the heap
        # create a min heap
        # sort by start time
        intervals.sort(key=lambda x: x.start)
        minHeap = []
        # iterate through the intervals
        for interval in intervals:
            start, end = interval.start, interval.end
            if minHeap and minHeap[0] <= start:
                heapq.heappop(minHeap)
            # push the end to the heap
            heapq.heappush(minHeap, end)
        return len(minHeap)

    # edge case
    # [(0, 1), (2, 3)]