class Solution:
    def validPalindrome(self, s: str) -> bool:
        # keep pointers at each ends 
        # if they mismatch, check if s[l:r-1] or s[l+1:r] is a palindrome or not
        # Time: O(n) from l and r moving to the center
        # Space: O(1)
        def checkPal(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                # print(s[l:r-1], s[l+1:r])
                # check skipping the right
                if checkPal(l, r-1) or checkPal(l+1, r):
                    return True
                return False
            l += 1
            r -= 1
        return True
        