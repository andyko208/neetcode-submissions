class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # create a counter of s
        s_counter = Counter(s) # Time: O(k), Space: O(k)
        # keep a pointer on order string and iterate through to build a string whenever the value on order string is in counter s and decrement that pointer to 0
        res = []
        for i in range(len(order)): # Time: O(N)
            if order[i] in s_counter:
                res.append(order[i] * s_counter[order[i]])
                s_counter[order[i]] = 0
        # iterate through the counter hashmap and append all letters > 0
        for char, count in s_counter.items(): # Time: O(k)
            if count > 0:
                res.append(char * count)
        return "".join(res)