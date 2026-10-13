class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Intuition: keep index i to move by len(word) of which word exists in s
        
        # Naive recursive -> runs TLE
        n = len(s)

        # Cache a 1D dp of False with size n
        # dp = [False] * (n+1)
        # dp[n] = True
        dp = {n: True}
        def dfs(i):
            # base case
            # if i == n:
            #     return True
            # if dp[i] != False:
            #     return dp[i]
            if i in dp:
                return dp[i]
            # iterate through to check whether valid word exists
            for w in wordDict:
                # check whether w appears from index i
                if s[i:i+len(w)] == w:
                    # check whether from there i can reach n
                    if dfs(i+len(w)):
                        # assign the value to dp list
                        dp[i] = True
                        return True
            # there is no set of words that moves index i to n
            dp[i] = False
            return False
        return dfs(0)