class Solution:
    def validPalindrome(self, s: str) -> bool:
        # keep pointers at each ends 
        # if they mismatch, check if s[l:r-1] or s[l+1:r] is a palindrome or not
        # Time: O(n) from l and r moving to the center
        # Space: O(1)
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                # print(s[l:r-1], s[l+1:r])
                if s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]:
                    return True
                return False
            l += 1
            r -= 1
        return True
        