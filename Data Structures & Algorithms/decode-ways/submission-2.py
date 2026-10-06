class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = dfs(i+1)
            if i+1 < n and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "01232456")):
                dp[i] += dfs(i+2)
            return dp[i]
        return dfs(0)

        # # Bottom up DP
        # n = len(s)
        # dp0, dp1, dp2 = 0, 1, 0
        # for i in range(n-1, -1, -1):
        #     if s[i] == "0":
        #         dp0 = 0
        #     else:
        #         dp0 = dp1
        #     if i+1 < n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
        #         dp0 += dp2
        #     dp0, dp1, dp2 = 0, dp0, dp1

        # return dp1


