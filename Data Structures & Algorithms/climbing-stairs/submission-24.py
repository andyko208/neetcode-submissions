class Solution:
    def climbStairs(self, n: int) -> int:
        # recurse to get the min of dfs(i+1) and dfs(i+2)
        # memoize using dp list of size n + 1 of -1
        dp = [-1] * n
        def dfs(i):
            # base case to return 1 only if i == n else 0
            if i >= n:
                return i == n
            # utilize memoized list to save work
            if dp[i] != -1:
                return dp[i]
            # update the memoized list
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        # start from 0
        return dfs(0)