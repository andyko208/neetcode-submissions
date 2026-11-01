class Solution:
    def countSubstrings(self, s: str) -> int:
        # Time: O(n^2), Space: O(n)
        # keep the same but just count now
        n = len(s)
        # 2D dp matrix for memoization
        # dp = [[0] * n for _ in range(n)]
        # keep two 1D lists to replace n x n grid
        prev, cur = [0] * n, [0] * n
        # keep a counter to count every valid palindromic string
        count = 0
        # iterate l from n to 0 
        for l in range(len(s)-1, -1, -1):
            # iterate r from l to n
            for r in range(l, n):
                # check if front and back are the same
                # or the size of substring <= 3, or memoized exists
                # if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                if s[l] == s[r] and (r - l <= 2 or prev[r-1]):
                    # update memoized list to 1
                    # dp[l][r] = 1
                    cur[r] = 1
                    # increment the count
                    count += 1
            # update the pointer for the next run
            prev, cur = cur, [0] * n
        return count
