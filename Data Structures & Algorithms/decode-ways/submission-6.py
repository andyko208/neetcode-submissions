class Solution:
    def numDecodings(self, s: str) -> int:
        # define dp list
        n = len(s)
        dp = [-1] * n
        # dp[n] = 1
        # recurse on index i
        def dfs(i):
            # base case to return 1 if i == n
            # return 0 if s[i]] == "0"
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            # return dp[i] if dp[i] != -1
            if dp[i] != -1:
                return dp[i]
            # dp[i] = recurse(i+1)
            dp[i] = dfs(i+1)
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                # recurse i+2 if possible to += dp[i] by it
                dp[i] += dfs(i+2)
            # return dp[i]
            return dp[i]
            # return dfs(0)
        return dfs(0)