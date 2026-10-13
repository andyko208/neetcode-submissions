class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)
        def dfs(i):
            if i >= n:
                return 0
            if dp[i] != 0:
                return dp[i]
            # return max(dfs(i+1), nums[i] + dfs(i+2))
            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return dp[i]
        return dfs(0)

        # take or skip
        # iterate through nums and decide when to take or skip

        # # initialize dp with n+2 and set n and n+1 to 0
        # n = len(nums)
        # # dp = [0] * (n+2)
        # # set dp1 and dp2 to 0
        # dp1, dp2 = 0, 0
        # # iterate i from n-1 to 0
        # for i in range(n-1, -1, -1):
        #     # set dp at i to the max between nums[i] + dp[i+2] and dp[i+1]
        #     # dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        #     tmp1 = dp1
        #     dp1 = nums[i] + dp2
        #     dp2 = max(tmp1, dp2)
        # # return the max of dp
        # return max(dp1, dp2)
        