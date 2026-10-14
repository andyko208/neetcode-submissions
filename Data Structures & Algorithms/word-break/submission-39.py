class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # n = len(s)
        # # optimize using memoization to store boolean value at index
        # dp = {}
        # dp[n] = True
        # # Time: O(N * max(wordDict, key=len) * len(wordDict))
        # # define dfs function that takes in i
        # def dfs(i):
        #     # base case to return True if i == n
        #     # if i == n:
        #     #     return True
        #     # iterate w in wordDict
        #     # memoization
        #     if i in dp:
        #         return dp[i]

        #     for w in wordDict:
        #         # if s[i:i+len(w)] == w
        #         if s[i:i+len(w)] == w:
        #             # if dfs(i+len(w)) == True
        #             if dfs(i+len(w)) == True:
        #                 dp[i] = True
        #                 return True
        #                 # return True
        #     # return False
        #     dp[i] = False
        #     return False
        # # return dfs(0)
        # return dfs(0)

        # Bottom-Up DP
        # memoize using hashmap and set dp{n: True}
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        # iterate from n-1 to -1
        for i in range(n-1, -1, -1):
            # iterate w in words to bring dp down to 0
            for w in wordDict:
                # if dp[i-len(w)] is also true, return true
                nextInd = i + len(w)
                if nextInd < n+1 and s[i:nextInd] == w:
                    dp[i] = dp[nextInd]
                    if dp[i]:
                        break
        return dp[0]



