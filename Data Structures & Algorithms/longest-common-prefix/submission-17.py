# class Node:
#     def __init__(self):
#         self.children = {}

# class Tree:
#     def __init__(self):
#         self.root = Node()
    
#     def add_word(self, word):
#         cur = self.root
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = Node()
#             cur = cur.children[c]
#         self.end = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # tree = Tree()
        # for s in strs:
        #     tree.add_word(s)
        # node = tree.root
        # i = 0
        # while node:
        #     if len(node.children) > 1:
        #         break
        #     i += 1
        #     node = node.children
        
        # # find the shortest string
        # iterate through the shorteset string
        for i in range(len(strs[0])):
            # iterate through s in str
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]