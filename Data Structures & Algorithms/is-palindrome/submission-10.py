class Solution:
    def isPalindrome(self, s: str) -> bool:
        # have a pointer l and r that points to 0 and n-1
        l, r = 0, len(s)-1
        # iterate through while l < r while checking chars at l and r are alphanum and lowercase them
        s = s.lower()
        while l < r:
            # move up each pointers to check between the valid chars
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            # return False whenever there's a mismatch, otherwise return True
            # if s[l].lower() != s[r].lower():
            if s[l] != s[r]:
                return False
            # move up each pointers after checking
            l, r = l + 1, r - 1
        return True