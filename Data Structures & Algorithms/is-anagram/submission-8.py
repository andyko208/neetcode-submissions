class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare the counter of each strings to return true if match else false
        # Time: O(s+t) from forming the counter hashmap
        # Space: O(s+t) from storing the counter hashmap
        return Counter(s) == Counter(t)