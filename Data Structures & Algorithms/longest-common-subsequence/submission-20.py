class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Recursion - Time: O(2^(m+n)), Space: O(m+n)
        # Top-Down DP - Time: O(m*n), Space: O(m*n)
        # define m and n
        m, n = len(text1), len(text2)
        # define a 2D matrix to store values from the recursive computation
        dp = [[0] * n for _ in range(m)]
        def dfs(i, j):
            # O(1) lookup for the previously computed recursive value
            if i ==m or j == n:
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            # recurse onto the next pointers if chars match
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i+1, j+1)
                return dp[i][j]
            # return the max of each recursive run
            dp[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            return dp[i][j]
        return dfs(0, 0)
        