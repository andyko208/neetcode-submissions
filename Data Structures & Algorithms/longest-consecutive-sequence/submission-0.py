class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # turn nums into a hashset
        nums_set = set(nums)
        max_seq = 0
        count = 0
        for num in nums:
            # find the first sequence 
            if num - 1 not in nums_set:
                first = num
                # while there is the next sequence, look up to increment the count
                while first in nums_set:
                    count += 1
                    first += 1
                max_seq = max(max_seq, count)
                count = 0
        return max_seq
