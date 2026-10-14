class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # optimize using memoization to store boolean value at index
        dp = {}
        dp[n] = True
        # define dfs function that takes in i
        def dfs(i):
            # base case to return True if i == n
            # if i == n:
            #     return True
            # iterate w in wordDict
            # memoization
            if i in dp:
                return dp[i]
                
            for w in wordDict:
                # if s[i:i+len(w)] == w
                if s[i:i+len(w)] == w:
                    # if dfs(i+len(w)) == True
                    if dfs(i+len(w)) == True:
                        dp[i] = True
                        return True
                        # return True
            # return False
            dp[i] = False
            return False
        # return dfs(0)
        return dfs(0)