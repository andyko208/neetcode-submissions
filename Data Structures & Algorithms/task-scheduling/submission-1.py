class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(n), Space: O(1)
        # define a mapping of counts of characters in tasks
        mapping = [0] * 26
        for t in tasks:
            mapping[ord(t) - ord('A')] += 1
        # get the max of the mapping count
        maxMap = max(mapping)
        maxCount = 0
        # find the count of maxes in mapping
        for m in mapping:
            if m == maxMap:
                maxCount += 1
        return max((maxMap - 1) * (n + 1) + maxCount, len(tasks))

