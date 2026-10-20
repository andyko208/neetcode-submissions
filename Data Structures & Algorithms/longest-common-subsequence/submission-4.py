class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Brute force
        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]
        # define a recursive function that takes in i and j
        def dfs(i, j):
            # base case to return 0 if i >= m or j >= n
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            # base case to return 1 if text1[i] == text2[j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i+1, j+1)
                return dp[i][j]
            # return max(dfs(i+1, j), dfs(i, j+1))
            dp[i][j] = max(dfs(i+1, j), dfs(i, j+1))
            return dp[i][j]
        # return dfs(0, 0)
        return dfs(0, 0)
