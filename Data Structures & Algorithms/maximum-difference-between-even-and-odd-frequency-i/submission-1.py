class Solution:
    def maxDifference(self, s: str) -> int:
        # maximum difference = biggest odd frequency - smallest even frequency
        # create a hashmap to accmulate counts of chars
        freq_map = Counter(s)
        # iterate through s to get the biggest odd and smallest even frequencies
        max_odd, min_even = 0, float('inf')
        for c, count in freq_map.items():
            # get the biggest odd count
            if count % 2 == 1:
                max_odd = max(count, max_odd)
            if count % 2 == 0:
                min_even = min(count, min_even)
        return max_odd - min_even
                
        