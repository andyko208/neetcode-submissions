class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 3 steps
        # Time: O(n) for iterating through the entire intervals
        # Space: O(n) for storing all intervals to return
        # define variables
        res = []
        i = 0
        n = len(intervals)
        # handle edge case
        if n == 0:
            return [newInterval]
        # append all intervals that ends b4 newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # merge all overlapping intervals to newInterval and append it at the end
        while i < n and newInterval[1] >= intervals[i][0]:
            # merge two intervals by setting the start to min and end to max
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        # append all intervals that comes after newInterval
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res

