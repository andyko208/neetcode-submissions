class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Brute force approach
        if len(s) == 1:
            return s
        pal = ""
        # iterate l from 0 to n-1
        for l in range(len(s)-1):
            # iterate r from n-1 to l+1 to check for the longest palindromic string
            for r in range(len(s)-1, l-1, -1):
                # if found and longer than current len of pal string, keep it and break
                substr = s[l:r+1]
                if substr == substr[::-1] and len(substr) > len(pal):
                    pal = substr
                    break
        return pal