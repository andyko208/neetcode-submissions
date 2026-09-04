class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # create a hashmap to map char of s to char of t
        s_map, t_map = {}, {}
        n = len(s)
        # iterate through and set hashmap[s[i]] = t[i]
        for i in range(n):
            s_map[s[i]] = t[i]
            t_map[t[i]] = s[i]
        # iterate again through s and turn each char into vals of the hashmap
        s_t, t_s = "", ""
        for i in range(n):
            s_t += s_map[s[i]]
            t_s += t_map[t[i]]
        return s_t == t and t_s == s
