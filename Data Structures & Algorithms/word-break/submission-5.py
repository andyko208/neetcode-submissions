class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # define a recursive function that takes in i to determine whether index starting at i and such word exists that brings i to i + len(word)
        # memoize by keeping {i: bool}
        memo = {len(s): True}
        def dfs(i):
            # base case to return False if i == len(s)
            # if i == len(s):
            #     return True
            if i in memo:
                return memo[i]
            # iterate through w in words and check if s[i + len(w)] == w
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    # if so, recurse from the next len: i + len(w)
                    if dfs(i + len(w)):
                        memo[i] = True
                        return memo[i]
            # otherwise this index fails
            memo[i] = False
            return memo[i]
        return dfs(0)
        
