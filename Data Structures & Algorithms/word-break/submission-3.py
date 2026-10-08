class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {len(s): True}
        def dfs(i):
            # base case to return true if we've reached the end of the string
            if i in memo:
                return memo[i]
            # check if all words are tere
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    if dfs(i+len(w)):
                        memo[i] = True
                        return memo[i]
            memo[i] = False
            return memo[i]
        return dfs(0)