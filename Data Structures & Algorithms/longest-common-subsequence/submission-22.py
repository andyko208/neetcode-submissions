class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Recursion - Time: O(2^(m+n)), Space: O(m+n)
        # Top-Down DP - Time: O(m*n), Space: O(m*n)
        # Bottom-Up DP - Time: O(m*n), Space: O(m*n)
        
        # define m and n
        m, n = len(text1), len(text2)
        # define a 2D matrix to store values from the recursive computation
        dp = [[0] * (n+1) for _ in range(m+1)]
        def dfs(i, j):
            # iterate i from m-1 to 0
            for i in range(m-1, -1, -1):
                # iterate j from n-1 to 0
                for j in range(n-1, -1, -1):
                    # set dp[i][j] from the next pointers of i and j if chars match
                    if text1[i] == text2[j]:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    # set dp[i][j] to be the max of next of either pointers if not
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        dfs(0, 0)
        return dp[0][0]
        