class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # m and n
        m, n = len(text1), len(text2)
        # create 2D DP matrix of size m by n
        dp = [[-1] * n for _ in range(m)]
        # define a recursive that takes i and j
        def dfs(i, j):
            # base case to return 0
            if i >= m or j >= n:
                return 0
            # memoization
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dfs(i+1, j+1)
                return dp[i][j]
            dp[i][j] = max(dfs(i, j+1), dfs(i+1, j))
            return dp[i][j]
        return dfs(0, 0)

        # abc ac
        # dp[0][0] = 1 + dfs(1, 1) = 2
        # dfs(1, 1)
        # dp[1][1] = max()
        # dfs(1, 2), dfs(2, 1)
        # dp[2][1] = 1 + dfs(3, 2) = 1
        # dp[1][1] = 1

        