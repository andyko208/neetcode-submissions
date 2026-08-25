class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute force approach: get the smallest length string O(N))
        # iterate through each strings to ensure the ith character of it matches with the rest        
        res = ""
        # get the minimum length string: O(N)
        n = len(strs)
        min_ind = 0
        # for i in range(n):
        #     if len(strs[i]) < len(strs[min_ind]):
        #         min_ind = i
        # count = 0
        strs.sort(key=len)
        shortest = strs[0]

        # # iterate through the minimum length string O(L)
        # for i in range(len(strs[min_ind])):
        #     # check for all the rest of the strings(don't have to check for all the strings, just with one)
        #     for j in range(n):
        #         if strs[j][i] != strs[min_ind][i]:
        #             return res
        #         count += 1
        #     if count == n:
        #         res += strs[min_ind][i]
        #     count = 0
        # return res

        # counter to determine whether to include the current char
        count = 0
        for i in range(len(shortest)):
            # check every string in the list
            for j in range(n):
                if strs[j][i] == shortest[i]:
                    count += 1
                # if match fails, no need to go further
                else:
                    return res
            if count == n:
                res += shortest[i]
            count = 0

        return res

        # if len(strs) <= 1:
        #     return strs[0]
        
        # strs.sort()
        # print(strs)
        
        # for i in range(len(strs[0])):
        #     print(strs[0], strs[-1])
        #     if strs[0][i] != strs[-1][i]:
        #         return strs[0][:i]
        
        # return strs[0]