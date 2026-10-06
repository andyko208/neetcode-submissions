class Solution:
    def countSubstrings(self, s: str) -> int:
        # # keep track of the count as we check for the palindromic string
        # n = len(s)
        # dp = [[0] * n for _ in range(n)]
        # count = 0
        # # iterate l from n-1 to -1
        # for l in range(n-1, -1, -1):
        #     # iterate r from l to n
        #     for r in range(l, n):
        #         # check if s[l] == s[r] and r - l <= 2:
        #         if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
        #             # dp[l][r] = dp[l+1][r-1] + 1
        #             dp[l][r] = 1
        #             count += 1
        # # return dp[0][len(s)-1]
        # return count

        # Two pointer
        # iterate i from 0 to n
        n = len(s)
        count = 0
        for i in range(n):
        # if check if l == r as we expand through while l and r are in valid range
            l, r = i, i
            # do this for each even and odd
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l, r = l - 1, r + 1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l, r = l - 1, r + 1
        return count
