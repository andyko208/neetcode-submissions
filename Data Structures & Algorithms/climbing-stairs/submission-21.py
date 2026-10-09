class Solution:
    def climbStairs(self, n: int) -> int:
        # recurse to get the min of dfs(i+1) and dfs(i+2)
        # base case to return 1 if i >= n
        # memoize using dp list of size n + 1 of -1
        dp = [-1] * (n+1)
        def dfs(i):
            if i >= n:
                return i == n
            if dp[i] != -1:
                return dp[i]
            # return dp[i] if != -1
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        # return dfs(0)
        return dfs(0)