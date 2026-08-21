class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time: O(N), Memory: O(N) 
        s1_map = Counter(s1)
        window = Counter()
        l = 0
        # print(s1_map)
        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                window[s2[l]] -= 1
                l += 1
            window[s2[r]] += 1
            if window == s1_map:
                return True
            # print(window)
        return False
