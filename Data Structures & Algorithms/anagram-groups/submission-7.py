class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap of list to group anagrams
        # set key as count list with 26 length -> O(1)
        # append strs[i] with same key as list

        # create a defaultdict list
        str_map = defaultdict(list)
        # iterate through s in strs
        for s in strs:
            # create a count map of list length 26
            count = [0] * 26
            # iterate through c in s
            for c in s:
                count[ord(c) - ord('a')] += 1
            # hashmap[count].append(s)
            # print(count)
            str_map[tuple(count)].append(s)
        # return hashmap.values()
        return list(str_map.values())
            