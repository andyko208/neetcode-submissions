class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Recursion - Time: O(2^(m+n)), Space: O(m+n)
        # Top-Down DP - Time: O(m*n), Space: O(m*n)
        # Bottom-Up DP - Time: O(m*n), Space: O(m*n)
        # Space-Optimized Bottom-Up DP - Time: O(m*n), Space: O(min(n, m))
        
        # define m and n
        m, n = len(text1), len(text2)
        # get the shorter length string to be text2
        if m < n:
            n, m = m, n
            text1, text2 = text2, text1
        # cur represents dp[i], prev dp[i+1]
        cur, prev = [0] * (n+1), [0] * (n+1)
        
        # iterate i from m-1 to 0
        for i in range(m-1, -1, -1):
            # iterate j from n-1 to 0
            for j in range(n-1, -1, -1):
                # translate dp[i][j] = 1 + dp[i+1][j+1] to cur and prev
                if text1[i] == text2[j]:
                    cur[j] = 1 + prev[j+1]
                # set dp[i][j] to be the max of next of either pointers if not
                else:
                    # translate dp[i][j] = max(dp[i+1][j], dp[i][j+1]) to cur and prev
                    cur[j] = max(cur[j+1], prev[j])
            # cur flows to prev: dp[i+1] -> dp[i] -> ... -> dp[0]
            prev = cur
            # reset cur
            cur = [0] * (n+1)
        # translate dp[0][0] to prev
        return prev[0]
        