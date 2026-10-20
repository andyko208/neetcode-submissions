class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(M*N), Space: O(M*N)
        # define 2D of size m x n
        dp = [[0] * n for _ in range(m)]
        # define a dfs function that takes in i and j
        def dfs(i, j):
            # base case to return 1 if i == m-1 and j == n-1
            if i == m-1 and j == n-1:
                return 1
            # base case to return 0 if i >= m or j >= n
            if i >= m or j >= n:
                return 0
            # perform a O(1) lookup using memoization
            if dp[i][j] != 0:
                return dp[i][j]
            # assign dp[i][j] as the recursive
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]
        return dfs(0, 0)