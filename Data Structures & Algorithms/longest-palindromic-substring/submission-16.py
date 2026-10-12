class Solution:
    def longestPalindrome(self, s: str) -> str:

        # iterate from 0 to n
        n = len(s)
        maxStr = ""
        maxLen = 0
        # expand left and right while they are valid
        for i in range(n):
            # update the string if the size of it is bigger
            # odd
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxStr = s[l:r+1]
                l -= 1
                r += 1
            # even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxStr = s[l:r+1]
                l -= 1
                r += 1
        return maxStr

