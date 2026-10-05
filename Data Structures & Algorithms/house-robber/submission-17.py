class Solution:
    def rob(self, nums: List[int]) -> int:
        # # Top down DP
        # # find the max of cur + cur + 2 recursive call or cur + 1 recursive call
        # dp = [-1] * len(nums)
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if dp[i] > -1:
        #         return dp[i]
        #     dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
        #     return dp[i]
        # return dfs(0)

        # # Bottom up DP
        # if len(nums) <= 1:
        #     return nums[0]
        # n = len(nums)
        # # build a cache list
        # dp = [-1] * n
        # dp[0] = nums[0]
        # dp[1] = max(dp[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        # return dp[-1]

        # Space optimized DP
        take = skip = 0
        for i in range(len(nums)):
            take, skip = nums[i] + skip, max(take, skip)
        return max(take, skip)


