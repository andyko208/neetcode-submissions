class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # create a 2D dp matrix of (m+1) x (n+1)
        # dp = [[0] * (n+1) for _ in range(m+1)]
        # def dfs(i, j):
        #     if i == m or j == n:
        #         return 1
        #     if dp[i][j] != 0:
        #         return dp[i][j]
        #     dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
        #     return dp[i][j]
        # return dfs(0, 0)
        dp = [[-1] * (n) for _ in range(m)]
        dp[m-1][n-1] = 1
        def dfs(i, j):
            # if i == m-1 and j == n-1:
            #     return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]

        return dfs(0, 0)