class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap of lists
        # sort each str in strs by lexicographic order O(N * M)
        # map each sorted str as key and append strs[i] to the hashmap
        # return values of the hashmap
        
        # create a hashmap
        str_map = defaultdict(list)
        # iterate through strs and sort strs[i] to map it to a key and value as strs[i]
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            str_map[key].append(strs[i])
        # return hashmap.values()
        # print(str_map)
        return list(str_map.values())