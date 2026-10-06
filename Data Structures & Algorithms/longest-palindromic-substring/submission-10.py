class Solution:
    def longestPalindrome(self, s: str) -> str:
        # get the len of s
        n = len(s)
        minL, maxR = 0, 0
        for i in range(n):
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > maxR - minL:
                    maxR, minL = r, l
                l, r = l - 1, r + 1
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > maxR - minL:
                    maxR, minL = r, l
                l, r = l - 1, r + 1
        return s[minL:maxR+1]
                        
        # if len is odd, set l and r to i and expand to get the max len window
        # if len is even, set l to i and r to i+1 and expand to get the max len window