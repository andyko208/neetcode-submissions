class Solution:
    def longestPalindrome(self, s: str) -> str:
        # keep a two DP list to tell whether dp[l][r] forms a valid palindrome
        # if i == j, fill up 1
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        maxLen = 1
        maxStr = s[0]
        # two for loops to iterate l and r
        for l in range(n-1, -1, -1):
            for r in range(l+1, n):
                if l == r:
                    dp[l][r] = 1
                elif s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = 1
                    if r - l + 1 > maxLen:
                        maxStr = s[l:r+1]
                        maxLen = r - l + 1
        return maxStr