class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-Up DP - Time: O(n), Space: O(n)
        # Space-Optimized - Time: O(n), Space: O(1)
        
        # create a 1D dp list of 0s
        dp = [0] * (n+2) # avoids index out of bounds
        dp[n] = 1

        # dp[i] -> cur, dp[i+1] -> prev1, dp[i+2] -> prev2
        cur, prev1, prev2 = 0, 1, 0

        # iterate i from n-1 to 0
        for i in range(n-1, -1, -1):
            # dp[i] = dp[i+1] + dp[i+2]
            cur = prev1 + prev2
            prev2, prev1, cur = prev1, cur, 0
        # return dp[0]
        return prev1