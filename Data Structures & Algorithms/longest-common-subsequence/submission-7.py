class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # create a recursive function dfs that takes in i and j
        m, n = len(text1), len(text2)
        # create a 2D matrix of size m x n
        dp = [[0] * n for _ in range(m)]
        # Time: O(2^n), Space: O(m+n)
        def dfs(i, j):
            # base case to return 0 if i >= m or j >= n
            if i >= m or j >= n:
                return 0
            # perform a look up
            if dp[i][j] != 0:
                return dp[i][j]
            # return 1 + dfs(i+1, j+1) if char of each text1 and text2 are the same
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i+1, j+1)
                return dp[i][j]
            # get the max of recursing on i+1, j and i, j+1
            dp[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            return dp[i][j]
        return dfs(0, 0)