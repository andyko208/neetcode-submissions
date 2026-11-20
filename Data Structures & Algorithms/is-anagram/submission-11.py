class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Intuition: compare the counter of each strings
        # Time: O(n+m) from forming the counter hashmap
        # Space: O(n+m) -> O(1) from storing the counter hashmap
        
        # hasmap approach
        # return Counter(s) == Counter(t)
        # Counter(s) = {a: 1}, Counter(t) = {a: 3}

        # array approach
        if len(s) != len(t):
            return False

        sSet, tSet = [0] * 26, [0] * 26
        for i in range(len(s)):
            sSet[ord('a') - ord(s[i])] += 1
            tSet[ord('a') - ord(t[i])] += 1
        # print(sSet, tSet)
        return sSet == tSet
        # sSet = [1, ..., 0], tSet[3, ..., 0]

    # edge case
    # s = "a", t= "aaa"