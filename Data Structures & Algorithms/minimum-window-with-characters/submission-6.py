class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep track of left and right
        # if we've found all substring permutation of t in s, trim from left
        # once the trimmed str is found, pop the leftmost to find the next substring
        # compare and get the minimum size of the substring
        l = 0
        n = len(s)
        s_counter, t_counter = Counter(), Counter(t)
        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(t_counter)
        for r in range(n):
            s_counter[s[r]] += 1
            # increment the substring char count
            if s[r] in t_counter and s_counter[s[r]] == t_counter[s[r]]:
                have += 1
            # trim from the left
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r+1]
                # if we are removing a valid substring from s_counter
                if s[l] in t_counter and s_counter[s[l]] == t_counter[s[l]]:
                    have -= 1
                s_counter[s[l]] -= 1
                l += 1
        l, r = res
        return s[l:r]

