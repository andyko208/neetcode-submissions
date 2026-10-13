class Solution:
    def rob(self, nums: List[int]) -> int:
        # take or skip
        # iterate through nums and decide when to take or skip

        # initialize dp with n+2 and set n and n+1 to 0
        n = len(nums)
        dp = [0] * (n+2)
        # iterate i from n-1 to 0
        for i in range(n-1, -1, -1):
            # set dp at i to the max between nums[i] + dp[i+2] and dp[i+1]
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        # return the max of dp
        return max(dp)
        