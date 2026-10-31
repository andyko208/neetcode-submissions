class Solution:
    def longestPalindrome(self, s: str) -> str:
        # define variables
        maxStr = ""
        # iterate through for loop from i=0 to n
        for i in range(len(s)):
            # expand for odd length case
            l, r = i, i
            # check whether pal chars on each end while staying bound
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # check if current window is bigger than cur max
                if r - l + 1 > len(maxStr):
                    maxStr = s[l:r+1]
                # expand the substring
                l, r = l - 1, r + 1
            # expand for even length case
            l, r = i, i+1
            # check whether pal chars on each end while staying bound
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # check if current window is bigger than cur max
                if r - l + 1 > len(maxStr):
                    maxStr = s[l:r+1]
                # expand the substring
                l, r = l - 1, r + 1

        return maxStr