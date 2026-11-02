class Solution:
    def numDecodings(self, s: str) -> int:
        # define variables
        n = len(s)
        # safe from index out of bounds in line 17
        dp = [0] * (n+1)
        # base case 
        dp[n] = 1
        # iterate i from n-1 to 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
            # base recursion
            dp[i] = dp[i+1]
            # only if two-digit is available
            if i + 1 < n:
                # 10-19
                if s[i] == "1" and s[i+1] in "0123456789":
                    dp[i] += dp[i+2]
                # 20-26
                elif s[i] == "2" and s[i+1] in "0123456":
                    dp[i] += dp[i+2]
        return dp[0]
