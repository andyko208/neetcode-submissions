class Solution:
    def numDecodings(self, s: str) -> int:
        # # start with the default case of s to the last index 1
        # n = len(s)
        # dp = {n: 1}
        # def dfs(i):
        #     # base case to return 
        #     # check if dp[i] is already there to return dp[i]
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0
        
        #     # by default, recurse on the next digit
        #     dp[i] = dfs(i+1)
        #     # if len > 2, recurse on the two digits
        #     if i+1 < n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
        #         dp[i] += dfs(i+2)
        #     return dp[i]
        # return dfs(0)

        # Bottom up DP
        n = len(s)
        dp = {n: 1}
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i+1 < n and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]

        return dp[0]


