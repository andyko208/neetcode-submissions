class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Intuition: keep index i to move by len(word) of which word exists in s
        
        # Top-Down DP
        # n = len(s)
        # memoize a 1D dp list of size n+1
        # dp = [-1] * (n+1)

        # def dfs(i):
        #     # base case
        #     if i == n:
        #         return True
        #     # return dp at i if not -1
        #     if dp[i] != -1:
        #         return bool(dp[i])
            
        #     # iterate through to check whether valid word exists
        #     for w in wordDict:
        #         # check whether w appears from index i
        #         if s[i:i+len(w)] == w:
        #             # check whether from there i can reach n
        #             if dfs(i+len(w)):
        #                 # assign boolean value dp as int at i
        #                 dp[i] = 1
        #                 return True
        #     # there is no set of words that moves index i to n
        #     # assign boolean value dp as int at i
        #     dp[i] = 0
        #     return False
        # return dfs(0)

        # Bottom-Up DP
        n = len(s)
        # memoize a 1D dp list of False
        dp = [False] * (n+1)
        # set dp[n] to True
        dp[n] = True
        # iterate through i from n-1 to 0
        for i in range(n-1, -1, -1):
            # iterate for w in wordDict
            for w in wordDict:
                nextInd = i + len(w)
                # check if i + len(w) is in valid range and s[i:i+len(w)] == w
                if nextInd < n+1 and s[i:nextInd] == w:
                    # if so, dp[i] = dp[i+len(w)]
                    dp[i] = dp[nextInd]
                    # if dp is True, since we've found one
                    if dp[i]:
                        break
        # return dp[0]
        return dp[0]


