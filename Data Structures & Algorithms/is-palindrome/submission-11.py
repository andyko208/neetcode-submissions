class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        # keep two pointers at each end
        l, r = 0, len(s)-1
        while l <= r:
            # move up the poiners while it sees non alnum
            while l < len(s) and not s[l].isalnum():
                l += 1
            while r > 0 and not s[r].isalnum():
                r -= 1
            # avoid index out of bounds
            if l > r:
                break
            # return False if any not match
            if s[l].lower() != s[r].lower():
                return False
            # update pointers
            l += 1
            r -= 1
        # return True at the end
        return True

# Edge case
# "a" -> True
# "ab" -> False
# "!!" -> False