class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force approach
        size = len(s1)
        if len(s2) < size:
            return False
        s1_map, s2_map = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_map[ord('a') - ord(s1[i])] += 1
            s2_map[ord('a') - ord(s2[i])] += 1
        l = 0
        print(s1_map)
        # create a counter for each s1 size window from s2
        for r in range(len(s2)):
            if r - l + 1 > size:
                s2_map[ord('a') - ord(s2[l])] -= 1
                s2_map[ord('a') - ord(s2[r])] += 1
                l += 1
            if s1_map == s2_map:
                return True
            # print(s2_map)
        return False