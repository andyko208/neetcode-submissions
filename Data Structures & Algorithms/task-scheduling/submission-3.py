class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(n), Space: O(1)
        # iterate through tasks to get countMap
        countMap = [0] * 26
        for t in tasks:
            countMap[ord('A') - ord(t)] += 1
        
        # get the max count value
        maxVal = max(countMap)
        # get the count of values that have max
        maxCount = 0
        for val in countMap:
            if val == maxVal:
                maxCount += 1
        # formula: # of gaps(maxVal-1) * # characters in that gap(n+1) + remaining chars(maxCount)
        return max(((maxVal-1) * (n+1) + maxCount), len(tasks))