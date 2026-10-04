class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        def dfs(index):
            if index >= n:
                return index == n
            if dp[index] != -1:
                return dp[index]
            dp[index] = dfs(index+1) + dfs(index+2)
            return dp[index]
        return dfs(0)        

