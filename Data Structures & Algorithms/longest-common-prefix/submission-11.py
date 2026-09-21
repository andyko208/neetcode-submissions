class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # get the min length of s in strs
        min_len = len(min(strs, key=len))
        # keep prefix str
        prefix = ""
        # while i < min length
        for i in range(min_len):
            for j in range(len(strs)-1):
                # iterate j in strs to check whether s[j][i] == s[j+1][i]
                if strs[j][i] != strs[j+1][i]:
                    # return prefix str if not eq
                    return prefix
            # outside the for loop add, prefix += s[j][i]
            prefix += strs[-1][i]
        return prefix
