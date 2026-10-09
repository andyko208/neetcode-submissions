class Solution:
    def countSubstrings(self, s: str) -> int:
        # keep the same but just count now
        # dp list to memoize the middle element being palindromic substring
        # keep a counter to check through as we go through
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        count = 0
        for l in range(len(s)-1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = 1
                    count += 1
        return count
