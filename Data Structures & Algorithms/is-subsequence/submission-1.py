class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # must contain all character from s in t
        # each letter found must be in relative order
        
        # keep a pointer at s and move t from 0 to len(t)

        s_ptr = 0
        # increment pointer s when char at pointer t == char at pointer s
        for i in range(len(t)):
            if s_ptr < len(s):
                if t[i] == s[s_ptr]:
                    s_ptr += 1
            else:
                return True
        # return true if pointer s is len(s)
        return True if s_ptr == len(s) else False