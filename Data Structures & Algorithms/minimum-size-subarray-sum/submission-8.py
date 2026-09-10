class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        min_len = float('inf')
        for r in range(len(nums)):
            # accumulate sum from l to r until >= target
            total += nums[r]
            # subtract from nums[l] while still >= target
            if total >= target:
                min_len = min(min_len, r - l + 1)
            while total - nums[l] >= target:
                total -= nums[l]
                l += 1
                min_len = min(min_len, r - l + 1)
            # print(nums[l:r+1])
        return min_len if min_len != float('inf') else 0
        