class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute force approach: get the smallest length string O(N))
        # iterate through each strings to ensure the ith character of it matches with the rest        
        res = ""
        # get the minimum length string: O(N)
        n = len(strs)
        min_ind = 0
        for i in range(n):
            if len(strs[i]) < len(strs[min_ind]):
                min_ind = i
        count = 0

        # iterate through the minimum length string O(L)
        for i in range(len(strs[min_ind])):
            # check for all the rest of the strings(don't have to check for all the strings, just with one)
            for j in range(n):
                if strs[j][i] != strs[min_ind][i]:
                    return res
                count += 1
            if count == n:
                res += strs[min_ind][i]
            count = 0
        return res
