class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # Bottom-Up DP
        # Intuition: dp[i] is true only if dp[i+len(valid_word)] is also true 

        n = len(s)
        # memoize a 1D dp list of False
        dp = [False] * (n+1)
        # set dp[n] to True
        dp[n] = True
        # iterate through i from n-1 to 0
        for i in range(n-1, -1, -1):
            # iterate for w in wordDict
            for w in wordDict:
                # end of the valid word from wordDict
                nextInd = i + len(w)
                # check if i+len(w) is in valid range and s[i:i+len(w)] is w
                if nextInd < n+1 and s[i:nextInd] == w:
                    # if so, dp[i] = dp[i+len(w)]
                    dp[i] = dp[nextInd]
                    # avoid looking for other words if already found
                    if dp[i]:
                        break
        return dp[0]


