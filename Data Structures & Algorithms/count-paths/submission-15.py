class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(2^N), Space: O(M+N)
        # optimize by adding memoization
        dp = [[0] * n for _ in range(m)]
        # define a dfs function that takes in i and j
        def dfs(i, j):
            # base case to return 1 if i == m-1 and j == n-1
            if i == m-1 and j == n-1:
                return 1
            # base case to return 0 if i >= m or j >= n
            if i >= m or j >= n:
                return 0
            # memoization
            if dp[i][j] != 0:
                return dp[i][j]
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]
        return dfs(0, 0)