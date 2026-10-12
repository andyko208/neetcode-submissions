class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * (n + 2)
        # for i in range(n-1, -1, -1):
        #     dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        # return dp[i]

        # space optimized
        n = len(nums)
        dp1, dp2 = 0, 0
        for i in range(n-1, -1, -1):
            tmp2 = dp2
            dp2 = dp1 + nums[i]
            dp1 = max(dp1, tmp2)
        return max(dp1, dp2)