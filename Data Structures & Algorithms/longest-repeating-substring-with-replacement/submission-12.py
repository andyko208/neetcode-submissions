class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # add to hashmap from left to right
        # check if the sum except the largest > k 
        # remove from l from min of rest < k
        charMap = {}
        l = 0
        total = 0
        maxLen = 0
        largestC = ""
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            while sum(charMap.values()) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen