class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time: O(n*m) where n is len(strs) and m is length of shortest str
        # Space: O(1)
        # iterate through the shorteset string
        for i in range(len(strs[0])):
            # iterate through s in str
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]


        # edge case
        # ["", "ab"]