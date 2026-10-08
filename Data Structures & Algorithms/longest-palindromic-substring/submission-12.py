class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # dp 
        # n = len(s)
        # # store a dp list to check whether middle element with l and r is 1
        # dp = [[0] * n for _ in range(n)]
        # ind, windowSize = 0, 0
        # # iterate l from n-1 to 0
        # for l in range(n-1, -1, -1):
        #     # iterate r from l to n
        #     for r in range(l, n):
        #         # check if s[l] == s[r] and len window <= 3 or dp[l+1][r-1]
        #         if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
        #             # dp[l][r] = 1
        #             dp[l][r] = 1
        #             # update ind, windowSize
        #             if r - l + 1 > windowSize:
        #                 ind = l
        #                 windowSize = r - l + 1
        # # return s[ind: ind+windowSize]
        # return s[ind:ind+windowSize]
        
        # cache a 2D dp list to tell middle elements dp[start][end] is valid
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ind, windowSize = 0, 0
        # iterate i from the end to 0 (left end)
        for l in range(n-1, -1, -1): 
            for r in range(l, n):
            # check if each ends are the same
                if s[l] == s[r]:
                    if r - l + 1 <= 3 or dp[l+1][r-1]:
                        dp[l][r] = 1
                        if r - l + 1 > windowSize:
                            ind = l
                            windowSize = r - l + 1
        return s[ind:ind+windowSize]