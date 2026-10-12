class Solution:
    def countSubstrings(self, s: str) -> int:
        # dynamic programming
        n = len(s)
        # create 2D dp list of 0s of size n
        dp = [[0] * n for _ in range(n)]
        # count variable
        count = 0
        # iterate l from n-1 to 0
        for l in range(n-1, -1, -1):
            # iterate r from i+1 to n
            for r in range(l, n):
                # check if s[l] == s[r] or dp[l+1][r-1] or r - l <= 2
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    # dp[l][r] = 1
                    dp[l][r] = 1
                    # count += 1
                    count += 1
        # return count
        return count