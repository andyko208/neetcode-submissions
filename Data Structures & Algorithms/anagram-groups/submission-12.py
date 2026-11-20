class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time: O(n * k log k) from iterating through and sorting
        # Space: O(n)
        # build a hashmap of sorted str: org str
        # return the values of the hashmap
        sMap = defaultdict(list)
        for s in strs:
            sMap["".join(sorted(s))].append(s)
        # print(sMap)
        return [s for s in sMap.values()]
