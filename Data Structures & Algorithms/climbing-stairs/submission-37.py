class Solution:
    def climbStairs(self, n: int) -> int:
        # create a 1D dp list of -1s
        dp = [0] * (n+2)
        dp[n] = 1
        # iterate i from n-1 to 0
        for i in range(n-1, -1, -1):
            # set dp[i] to be the sum of dp[i+1] and dp[i+2]
            dp[i] = dp[i+1] + dp[i+2]
        # return dp[0]
        return dp[0]