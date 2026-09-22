class Solution:
    def validPalindrome(self, s: str) -> bool:
        # keep pointers l and r 
        l, r = 0, len(s)-1
        # iterate through while l < r
        while l < r:
            # check if s[l] != s[r]
            if s[l] != s[r]:
                # return True if removing left or removing right makes a valid palindrom
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
            l += 1
            r -= 1
        return True
