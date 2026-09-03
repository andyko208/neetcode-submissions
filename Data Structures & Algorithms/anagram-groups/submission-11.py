class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create str_hash of lists
        str_hash = defaultdict(list)
        # iterate through s in strs
        for s in strs:
            # create a key as [0] * 26 of character filled with 1s
            cMap = [0] * 26
            # iterate through c in s
            for c in s:
                cMap[ord('a') - ord(c)] += 1
            str_hash[tuple(cMap)].append(s)
            # iterate through strs and append word to appropriate key
        return list(str_hash.values())