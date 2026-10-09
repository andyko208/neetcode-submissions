class Solution:
    def countSubstrings(self, s: str) -> int:
        # keep the same but just count now
        n = len(s)
        # dp list to memoize the middle element being palindromic substring
        dp = [[0] * n for _ in range(n)]
        # keep a counter to increment for every palindromic string found
        count = 0
        # iterate l from n to 0 
        for l in range(len(s)-1, -1, -1):
            # iterate r from l to n
            for r in range(l, n):
                # check if front and back are the same
                # or the size of substring <= 3, or memoized exists
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    # update the current l and r pointer in the memoized list to 1
                    dp[l][r] = 1
                    # increment the count
                    count += 1
        return count
