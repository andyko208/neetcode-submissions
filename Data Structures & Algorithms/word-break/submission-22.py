class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # cache a hashmap with n: True
        dp = {n: True}
        def dfs(i):
            # base case to return 
            if i in dp:
                return dp[i]
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return dfs(0)