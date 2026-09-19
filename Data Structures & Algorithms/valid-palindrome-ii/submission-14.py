class Solution:
    def validPalindrome(self, s: str) -> bool:
        # keep pointers l and r at 0 and n-1
        n = len(s)
        l, r = 0, n-1
        while l < r:
            # truncate off to get the slice and compare both of them whether their reverse are the same
            if s[l] != s[r]:
                return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
            l, r = l + 1, r - 1
        return True