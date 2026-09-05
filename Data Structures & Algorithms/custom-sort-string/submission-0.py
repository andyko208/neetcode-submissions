class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # create a Counter hashmap of s
        s_map = Counter(s)
        order_map = Counter(order)
        res = ""
        # iterate through order string and append the character that exists in the counter hashmap
        for i in range(len(order)):
            if order[i] in s_map:
                res += order[i] * s_map[order[i]]
        # iterate back again through s to get the ones that are not in the counter hashmap and append
        for i in range(len(s)):
            if s[i] not in order_map:
                res += s[i]
        return res
