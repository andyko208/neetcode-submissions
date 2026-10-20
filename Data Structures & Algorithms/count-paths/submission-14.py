class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(2^n), Space: O(m*n)
        # define dfs that takes in i and j
        # memoization 
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        def dfs(i, j):
            # base case to return 1 at i==m-1 and j==n-1
            # if i==m-1 and j==n-1:
            #     return 1
            # base case to return 0 at i>=m or j >=n
            if i >= m or j >= n:
                return 0

            if dp[i][j] != 0:
                return dp[i][j]
            # return the sum of dfs(i+1, j) and dfs(i, j+1)
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]
        return dfs(0, 0)