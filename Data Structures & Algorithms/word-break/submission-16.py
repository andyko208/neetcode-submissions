class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # recursively pass the next index of which i + len(word) of that exists
        n = len(s)
        dp = {n: True}
        def dfs(i):
            # base case to return True
            # if i == n:
            #     return True
            if i in dp:
                return dp[i]
            # iterate through to check whether valid word exists
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return dfs(0)