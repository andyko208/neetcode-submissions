class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom-Up DP
        m, n = len(text1), len(text2)
        # dp matrix of size m x n of 0s
        dp = [[0] * (n+1) for _ in range(m+1)]
        # iterate i from m-1 to 0
        for i in range(m-1, -1, -1):
            # iterate j from n-1 to 0
            for j in range(n-1, -1, -1):
                # if text1[i] == text2[j]
                if text1[i] == text2[j]:
                    # update dp[i][j] to 1 + dp[i+1][j+1]
                    dp[i][j] = 1 + dp[i+1][j+1]
                # else
                else:
                    # update dp[i][j] to be the max of dp[i+1][j], dp[i][j+1]
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]
        return dp[0][0]
        
        