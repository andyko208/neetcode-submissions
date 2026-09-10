class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute force approach
        s1_map = [0] * 26
        for c in s1:
            s1_map[ord('a') - ord(c)] += 1
        s1_counter = Counter(s1)
        size = len(s1)
        # create a counter for each s1 size window from s2
        for i in range(len(s2)-size+1):
            charMap = [0] * 26
            for j in range(i, i+size):
                # print(i, j)
                charMap[ord('a') - ord(s2[j])] += 1
            if charMap == s1_map:
                return True
        return False