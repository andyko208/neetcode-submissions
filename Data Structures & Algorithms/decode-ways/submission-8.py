class Solution:
    def numDecodings(self, s: str) -> int:
        # # recurse through the index of i such that each dfs(i) returns the count at i
        # # define a dfs(i)
        # def dfs(i):
        #     # base case returns 1 if i == n
        #     if i == len(s):
        #         return 1
        #     # base case reutrn 0 if s[i] == "0"
        #     if s[i] == "0":
        #         return 0
        #     # res = dfs(i+1)
        #     res = dfs(i+1)
        #     # if i + 1 < n and s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"
        #     if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
        #         # res += dfs(i+2)
        #         res += dfs(i+2)
        #     # return res
        #     return res
        # # return dfs(0)
        # return dfs(0)

        # # Top down DP
        # # cache a list of dp of length len(s) where dp[i] represents the count
        # dp = [-1] * len(s)
        # # define a recursive function that takes in i
        # def dfs(i):
        #     # base case to return 1 if i == n
        #     if i == len(s):
        #         return 1
        #     # base case to return dp[i] if dp[i] != -1
        #     if dp[i] != -1: 
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0
        #     # perform a top-down recursive call
        #     dp[i] = dfs(i+1)
        #     # if str is between 10-26, dp[i] += dfs(i+2)
        #     if i + 1 < n and (s[i] == "1" or s[i] == "2" and s[i+1] == "01234546"):
        #         dp[i] += dfs(i+2)
        #     # return dp[i]
        #     return dp[i]
        # # return dfs(0)
        # return dfs(0)

        # Bottom up DP
        n = len(s)
        # cache a dp list of len n
        dp = [-1] * (n + 1)
        # dp[n] = 1
        dp[n] = 1
        # iterate from i in range(n-1, -1, -1):
        for i in range(len(s)-1, -1, -1):
            # dp[i] = dp[i+1]
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            # if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                # dp[i] += dp[i+2]
                dp[i] += dp[i+2]
        # return dp[len(s)]
        return dp[0]







