class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # keep a pointer for t t_ptr
        t_ptr = 0
        # iterate through s and check if t_ptr < len(t) 
        for i in range(len(s)):
            if t_ptr < len(t):
                # if s[i] == t[t_ptr] to increment t_ptr by 1 and needed_count -= 1
                if s[i] == t[t_ptr]:
                    t_ptr += 1
            # else, we've found all chars of t in s
            else: 
                break
        # return len(t) - t_ptr
        return len(t) - t_ptr