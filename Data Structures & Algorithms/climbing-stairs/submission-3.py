class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive 
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     return dfs(i+1) + dfs(i+2)
        # return dfs(0)
        
        # top down DP
        dp = [0] * n
        # set up the base cases
        def dfs(i):
            if i >= n:
                return i==n
            if dp[i] != 0:
                return dp[i]
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        
        return dfs(0)