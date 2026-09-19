class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len is not the same, return false
        if len(s) != len(t):
            return False
        # build a hashmap for s and t at the same time and make comparisons
        s_map, t_map = {}, {}
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1
            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 1
        # whether the number of character in s is the same as t
        return s_map == t_map
            
