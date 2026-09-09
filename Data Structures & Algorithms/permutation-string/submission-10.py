class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force approach
        s1_counter = Counter(s1)
        size = len(s1)
        # create a counter for each s1 size window from s2
        for i in range(len(s2)-size+1):
            if Counter(s2[i:i+size]) == s1_counter:
                return True
        return False
        # s1_map = Counter(s1)
        # s1_len = len(s1)
        # # keep a s1 sized sliding window at s2
        # l = 0
        # # remove leftmost element if not in s1_map, increment l and append s[r]
        # for r in range(len(s2)):
        #     if s2[r] in s1_map:
        #         s1_map[s2[r]] -= 1
        #         if s1_map[s2[r]] < 0:
        #             return False
        #     if r - l + 1 > s1_len:

            
        # # return false if any element of s1_map gets < 0
        # # subtract the count of s[r] from s1_map
