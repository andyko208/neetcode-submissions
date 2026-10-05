class Solution:
    def climbStairs(self, n: int) -> int:
        # # recursive
        # def dfs(i):
        #     if i >= n:
        #         return 1 if i == n else 0
        #     return dfs(i+1) + dfs(i+2)
        # return dfs(0)

        # Top down
        dp = [-1] * (n+1)
        def dfs(i):
            if i >= n:
                return i==n
            if dp[i] != -1:
                return dp[i]
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        return dfs(0)

            