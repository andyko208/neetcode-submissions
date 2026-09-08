class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase and remove all spaces of s and the punctuations
        s_new = []
        for i in range(len(s)):
            if s[i].isalnum():
                s_new.append(s[i].lower())
        s_str = "".join(s_new)
        # iterate one pointer from 0 and the other from n-1
        n = len(s_str)
        for i in range(n//2):
            if s_str[i] != s_str[n-i-1]:
                return False
        # check if s[l] and s[r] are the same, return False if not
        return True
        