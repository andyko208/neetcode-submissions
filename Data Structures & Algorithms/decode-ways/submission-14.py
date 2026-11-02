class Solution:
    def numDecodings(self, s: str) -> int:
        # define a recursive function to return the count
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        prev2, prev1, cur = 0, 1, 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                cur = 0
            else:
                dp[i] = dp[i+1]
                cur = prev1
                if i + 1 < n:
                    if s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"):
                        dp[i] += dp[i+2]
                        cur += prev2
            prev2, prev1, cur = prev1, cur, 0
        return prev1