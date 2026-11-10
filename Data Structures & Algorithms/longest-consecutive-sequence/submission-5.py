class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn nums into a hashset
        numSet = set(nums)
        visited = set()
        maxCount = 0
        # find the start of the sequence and keep -1
        for num in numSet:
            if num in visited:
                continue
            while num-1 in numSet:
                num -= 1
            # iterate until value +1 is there
            count = 1
            while num+1 in numSet:
                num += 1
                count += 1
                visited.add(num)
            maxCount = max(maxCount, count)
        return maxCount