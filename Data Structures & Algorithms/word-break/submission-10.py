class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom Up approach
        # memoize a list of False of len n
        n = len(s)
        dp = [False] * (n+1)
        # intialize dp[n] = True
        dp[n] = True
        # iterate from n-1 to 0
        for i in range(n-1, -1, -1):
            # iterate from w in wordDict
            for w in wordDict:
                # if i + len(w) <= len(w) and s[i:i+len(w)] == w
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                # check if dp[i] to break
                if dp[i]:
                    break
        # return dp[0]
        return dp[0]