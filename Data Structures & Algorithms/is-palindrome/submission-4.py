class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # lowercase and remove all spaces of s and the punctuations
        # s_new = []
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         s_new.append(s[i].lower())
        # s_str = "".join(s_new)
        # # iterate one pointer from 0 and the other from n-1
        # n = len(s_str)
        # for i in range(n//2):
        #     if s_str[i] != s_str[n-i-1]:
        #         return False
        # # check if s[l] and s[r] are the same, return False if not
        # return True

        # keep two pointers l and r
        l, r = 0, len(s)-1
        # iterate while l < r
        while l < r:
            # check if s[l] and s[r] is alnum
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            # check for the lower case of s[l] and s[r]
            if s[l].lower() != s[r].lower():
                return False
            # increment l and decrement r
            l, r = l + 1, r - 1
        return True
        