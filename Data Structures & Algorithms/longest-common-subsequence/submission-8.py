class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom up DP
        # Time: O(M*N), Space: O(M*N)
        m, n = len(text1), len(text2)
        # create dp of size m+1 by n+1
        dp = [[0] * (n+1) for _ in range(m+1)]
        # iterate i from n-1 to 0
        for i in range(m-1, -1, -1):
            # iterate j from m-1 to 0
            for j in range(n-1, -1, -1):
                # if text1[i] == text2[j], 1 + dp[i+1][j+1]
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                # else dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        # return dp[0][0]
        return dp[0][0]