class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Intuition: iterate through all the words and check if they exist and can recurse through after picking the valid word
        
        # # Naive recursive -> runs TLE
        # n = len(s)
        # def dfs(i):
        #     # base case
        #     if i == n:
        #         return True
        #     # iterate through to check whether valid word exists
        #     for w in wordDict:
        #         if s[i:i+len(w)] == w:
        #             # check whether from there i can reach n
        #             if dfs(i+len(w)):
        #                 return True
        #     return False
        # return dfs(0)
        
        # keep a cache hashmap with base case True at n
        n = len(s)
        dp = {n: True}
        def dfs(i):
            # if previously mapped, return the dp at i
            if i in dp:
                return dp[i]
            # iterate through to check whether valid word exists
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    # check whether from there i can reach n
                    if dfs(i+len(w)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return dfs(0)