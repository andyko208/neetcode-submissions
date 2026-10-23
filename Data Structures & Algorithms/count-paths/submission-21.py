class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Recursion - Time: O(2^(n+m)), Space: O(m+n)
        # Top-Down DP - Time: O(m*n), Space: O(m*n)
        dp = [[-1] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        def dfs(i, j):
            if i == m or j == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            # if i == m-1 and j == n-1:
            #     return 1
            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dp[i][j]
        
        return dfs(0, 0)
