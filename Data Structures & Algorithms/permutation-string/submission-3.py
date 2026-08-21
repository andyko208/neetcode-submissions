class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # # naive approach O(NM)
        # # keep creating a counter from s2 of len s1 by iterating r from 0 to n-len(s1)
        # s1_counter = Counter(s1)
        # l = 0
        # for r in range(len(s2)-len(s1)+1):
        #     if s1_counter == Counter(s2[r:r+len(s1)]):
        #         return True
        # return False

        # maintain a window of size len(s1)
        # keep adding chars from s2 until its length goes bigger than len(s1)
        # check if set(s1) == window
        # if not, move L by 1 and remove the leftmost item
        s1_map = Counter(s1)
        window = Counter()
        l = 0
        print(s1_map)
        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                window[s2[l]] -= 1
                l += 1
            window[s2[r]] += 1
            if window == s1_map:
                return True
            print(window)
        return False
