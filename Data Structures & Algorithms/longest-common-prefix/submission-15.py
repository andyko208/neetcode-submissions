# class Node:
#     def __init__(self, val):
#         self.val = None
#         self.next = None

# class Tree:
#     def __init__(self):
#         self.values = {}
#         self.end = False
    
#     def add_word(self, word):
#         cur = self.values
#         for c in word:
#             if c not in cur:
#                 cur[c] = Node(c)
#             cur = cur[c].next
#         self.end = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # tree = Tree()
        # for s in strs:
        #     tree.add_word(s)
        # print(tree.values)
        
        # find the shortest string
        shortest = min(strs, key=len)
        if len(shortest) == 1:
            return shortest
        ind = 0
        # iterate through the shorteset string
        for i in range(len(shortest)):
            # iterate through s in str
            for s in strs:
                # return shortest string up to the index
                if shortest[i] != s[i]:
                    return shortest[:i]
            ind = i
        return "" if ind == 0 else shortest[:ind+1]