class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom-Up DP
        m, n = len(text1), len(text2)
        # let text1 be bigger len string and text2 be smaller
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m
        # dp matrix of size m x n of 0s
        # dp = [[0] * (n+1) for _ in range(m+1)]
        # turn 2D dp matrix into prev(i+1) and cur(i) of size min(m, n)
        prev, curr = [0] * (n+1), [0] * (n+1)
        # iterate i from m-1 to 0
        for i in range(m-1, -1, -1):
            # iterate j from n-1 to 0
            for j in range(n-1, -1, -1):
                # if text1[i] == text2[j]
                if text1[i] == text2[j]:
                    # update dp[i][j] to 1 + dp[i+1][j+1]
                    # dp[i][j] = 1 + dp[i+1][j+1]
                    curr[j] = 1 + prev[j+1]
                # else
                else:
                    # update dp[i][j] to be the max of dp[i+1][j], dp[i][j+1]
                    # dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    curr[j] = max(prev[j], curr[j+1])
            curr, prev = prev, curr
        # return dp[0][0]
        return prev[0]
        
        