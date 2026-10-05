class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        def rob2(nums):
            take = skip = 0
            for i in range(len(nums)):
                take, skip = nums[i] + skip, max(take, skip)
            return max(take, skip)
        return max(rob2(nums[:-1]), rob2(nums[1:]))

