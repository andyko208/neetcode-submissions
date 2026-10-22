class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time: O(M*N), Space: O(M*N)
        # 2D dp matrix of size m x n of 0s
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # prevent going out of bounds
                right = dp[i+1][j] if i+1 < m else 0 
                bottom = dp[i][j+1] if j+1 < n else 0
                dp[i][j] += right + bottom
        return dp[0][0]