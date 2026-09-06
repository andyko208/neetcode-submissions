class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # create a Counter hashmap of s
        s_map = Counter(s)
        order_map = Counter(order)
        res = []
        # Time: O(N + k), Space: O(N + k)
        # iterate through order string and append the character that exists in the counter hashmap
        for i in range(len(order)):
            if order[i] in s_map:
                res.append(order[i] * s_map[order[i]])
        # iterate back again through s to get the ones that are not in the counter hashmap and append
        for i in range(len(s)):
            if s[i] not in order_map:
                res.append(s[i])
        return "".join(res)
