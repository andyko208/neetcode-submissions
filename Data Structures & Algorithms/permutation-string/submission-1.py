class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # naive approach O(N)
        # keep creating a counter from s2 of len s1 by iterating r from 0 to n-len(s1)
        s1_counter = Counter(s1)
        l = 0
        for r in range(len(s2)-len(s1)+1):
            if s1_counter == Counter(s2[r:r+len(s1)]):
                return True
        return False