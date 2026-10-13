class Solution:
    def climbStairs(self, n: int) -> int:
        # # define a recursive function that takes in i(curr value)
        # dp = [-1] * (n+1)
        # # dp[n] = 1
        # def dfs(i):
        #     # base case to return 0 if i > n
        #     if i > n:
        #         return 0
        #     # base case to return 1 if i == n
        #     if i == n:
        #         return 1
        #     # memoization
        #     if dp[i] != -1:
        #         return dp[i]
        #     # return dfs(i+1) or dfs(i+2)
        #     dp[i] = dfs(i+1) + dfs(i+2)
        #     return dp[i]
        # return dfs(0)

        # sum of taking 1 + taking 2
        dp = [0] * (n+1)
        dp[n] = 1
        dp[n-1] = 1
        # walk backwards
        for i in range(n-2, -1, -1):
            dp[i] = dp[i+1] + dp[i+2]
        # return max(dp)
        return dp[0]





