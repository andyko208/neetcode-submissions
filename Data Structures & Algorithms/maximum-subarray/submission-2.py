class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEnd = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            # set whether to start new or include prev seq
            maxEnd = max(maxEnd + nums[i], nums[i])
            res = max(res, maxEnd)
        return res