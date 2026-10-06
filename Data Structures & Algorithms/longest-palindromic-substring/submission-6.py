class Solution:
    def longestPalindrome(self, s: str) -> str:
        # define ind and windowSize
        ind, windowSize = 0, 0
        n = len(s)
        # create a 2D DP list that tells whether middle element [l:r] is pal
        dp = [[0] * n for _ in range(n)]
        # iterate i from n-1 to 0
        for l in range(n-1, -1, -1):
            # iterate j from i to n
            for r in range(l, n):
                # check if s[i] == s[j] and dp list is valid or len <= 3
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]==1):
                    dp[l][r] = 1
                    # update ind and windowSize if curr > windowSize
                    if r - l + 1 > windowSize:
                        ind = l
                        windowSize = r - l + 1
                    # if l + 1 < n and r - 1 > 0:
                        # print(dp[l+1][r-1])
                    # print(l, s[l], r, s[r], ind, windowSize)


        # return s[ind:ind+windowSize]
        return s[ind:ind+windowSize]
