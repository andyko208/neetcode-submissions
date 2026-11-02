class Solution:
    def numDecodings(self, s: str) -> int:
        # Bottom-Up - Time: O(n), Space: O(1)
        # define variables
        n = len(s)
        # dp[i+2], dp[i+1], dp[i]
        prev2, prev1, cur = 0, 1, 0
        # iterate i from n-1 to 0
        for i in range(n-1, -1, -1):
            # ignore leading zeros
            if s[i] == '0':
                cur = 0
            else:
                # base recursion
                cur = prev1
                # only if two-digit is available
                if i + 1 < n:
                    # 10-19 or 20-26
                    if s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"):
                        # dp[i] += dp[i+2]
                        cur += prev2
            # update for next iteration
            prev2, prev1, cur = prev1, cur, 0
        # return dp[0]
        return prev1
