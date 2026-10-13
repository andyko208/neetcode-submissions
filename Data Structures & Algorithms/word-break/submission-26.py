class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Intuition: keep index i to move by len(word) of which word exists in s
        
        # Naive recursive -> runs TLE
        n = len(s)

        # Cache a 1D dp of False with size n
        dp = [-1] * (n+1)
        dp[n] = 1
        def dfs(i):
            # base case
            # if i == n:
            #     return True
            if dp[i] != -1:
                return bool(dp[i])
            # iterate through to check whether valid word exists
            for w in wordDict:
                # check whether w appears from index i
                if s[i:i+len(w)] == w:
                    # check whether from there i can reach n
                    if dfs(i+len(w)):
                        # assign the value to dp list
                        dp[i] = 1
                        return bool(dp[i])
            # there is no set of words that moves index i to n
            dp[i] = 0
            return bool(dp[i])
        return dfs(0)