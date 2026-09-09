class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a hashmap
        window_map = defaultdict(int)
        l = 0
        max_count = 0
        max_len = 0
        for r in range(len(s)):
            # add s[r] to the hashmap
            window_map[s[r]] += 1
            # keep max character count in the window
            max_count = max(max_count, window_map[s[r]])
            # while the window size is not valid, remove from the left element
            while r - l + 1 - max_count > k:
                window_map[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
