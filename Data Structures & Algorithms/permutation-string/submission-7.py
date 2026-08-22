class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # naive solution is to create counter at each element
        # check if the counter of that is the same as s1
        l = 0
        s1_counter = Counter(s1)
        for r in range(len(s2)-len(s1)+1):
            s2_counter = Counter(s2[r:r+len(s1)])
            print(s1_counter, s2_counter)
            if s1_counter == s2_counter:
                return True
        return False