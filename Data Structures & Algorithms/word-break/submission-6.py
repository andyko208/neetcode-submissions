class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom Up Dp
        # keep a dp list and initilaize len(s) = 1
        n = len(s)
        dp = [False] * (n+1)
        dp[len(s)] = True
        i = 0
        # iterate through and check for word in words for the condition
        for i in range(n-1, -1, -1):
            for w in wordDict:
                # if dp[i+len(w)] is also there, return True
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        # else return False
        return dp[0]
            