class Solution:
    def longestPalindrome(self, s: str) -> str:
        # define n
        n = len(s)
        # define a 2D dp matrix of 0s of n x n
        # dp = [[0] * n for _ in range(n)]
        # prev, cur
        prev, cur = [0] * n, [0] * n
        # keep maxLen and index
        index, maxLen = 0, 0
        # iterate l from n-1 to 0
        for l in range(n-1, -1, -1):
            # iterate r from l to n
            for r in range(l, n):
                # determine whether substring from l to r is palindromic
                # if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                if s[l] == s[r] and (r - l <= 2 or prev[r-1]):
                    # it's a valid palindromic substring
                    # dp[l][r] = 1
                    cur[r] = 1
                    # keep track of the max len and update the index
                    if r - l + 1 > maxLen:
                        index = l
                        maxLen = r - l + 1
            prev = cur
            cur = [0] * n
        # return the max palindromic substring using index and maxLen
        return s[index:index+maxLen]