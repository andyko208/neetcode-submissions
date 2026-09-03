class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # keep a pointer for s
        s_ptr = 0
        # iterate through t
        for i in range(len(t)):
        # if s_ptr < len(s)
            if s_ptr < len(s) and s[s_ptr] == t[i]:
                # increment s_ptr by 1 if s[s_ptr] == t[i]
                s_ptr += 1
            # return True if s_ptr == len(s) else False
        return True if s_ptr == len(s) else False