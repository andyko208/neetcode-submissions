class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Recursion - Time: O(2^(n+m)), Space: O(m+n)
        # Top-Down DP - Time: O(m*n), Space: O(m*n)
        # Bottom-Up DP - Time: O(m*n), Space: O(m*n)
        # BU DP Space optimized - Time: O(m*n), Space: O(n)
        
        # dp = [[0] * (n+1) for _ in range(m+1)]
        curr, prev = [0] * (n+1), [0] * (n+1)
        # dp[m-1][n-1] = 1
        # prev[n-1] = 1
        curr[n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # dp[i][j] += dp[i+1][j] + dp[i][j+1]
                curr[j] += prev[j] + curr[j+1]
            prev = curr
            curr = [0] * (n+1)
        return prev[0]