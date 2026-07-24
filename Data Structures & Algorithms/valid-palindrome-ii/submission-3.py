class Solution:
    def validPalindrome(self, s: str) -> bool:

        # keep pointers l and r, iterate through while l < r
        l, r = 0, len(s)-1
        # if s[l] != s[r], determine whether to check palidrome from s[l+1:r+1](remove l) or s[l:r](remove r)
        while l < r:
            if s[l] != s[r]:
                return s[l+1:r+1]== s[l+1:r+1][::-1] or s[l:r]==s[l:r][::-1]
            l, r = l + 1, r - 1
        return True
        # check palindrome of the removed l or removed r