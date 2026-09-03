class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        # create two hash maps and track each character with count
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        # iterate i through len(s)
        for i in range(len(s)):
            # add each char and count to the hashmap
            s_hash[s[i]] += 1
            t_hash[t[i]] += 1
        return s_hash == t_hash