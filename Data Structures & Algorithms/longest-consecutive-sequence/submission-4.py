class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n), Space: O(n)
        # turn nums into a hashset
        numSet = set(nums)
        visited = set()
        maxCount = 0
        # find the start of the sequence and keep -1
        for num in numSet:
            while num-1 in numSet and num-1 not in visited:
                num -= 1
            # iterate until value +1 is there
            count = 1
            while num+1 in numSet and num+1 not in visited:
                num += 1
                count += 1
                visited.add(num)
            maxCount = max(maxCount, count)
        return maxCount