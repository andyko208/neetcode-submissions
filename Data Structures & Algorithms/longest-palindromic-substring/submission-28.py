class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Intution: update the start window and the window size for longer palindromes
        # Time: O(n*2), Space: O(n)
        n = len(s)
        # cache a 2D dp list to tell middle elements from l to r forms a palindrome
        dp = [[0] * n for _ in range(n)]
        # instead of a 2D dp list, we can keep 2 1D dp lists to do the same
        prev, cur = [0] * n, [0] * n
        # initial values to start with
        ind, windowSize = 0, 0
        # iterate l from the end to 0 (left end)
        for l in range(n-1, -1, -1): 
            # itereate r from l to end
            for r in range(l, n):
                # check if each ends are the same
                if s[l] == s[r]:
                    # conditions for which elements b/ l&r are automatically palindrome
                    # if r - l + 1 <= 3 or dp[l+1][r-1]:
                    if r - l + 1 <= 3 or prev[r-1]:
                        # update the cache
                        # dp[l][r] = 1
                        cur[r] = 1
                        # update the index and window size
                        if r - l + 1 > windowSize:
                            ind = l
                            windowSize = r - l + 1
            prev = cur
            cur = [0] * n
        return s[ind:ind+windowSize]