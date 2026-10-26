# construct a trie node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    def add_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # construct trie nodes of from the list of words
        pTree = PrefixTree()
        for w in words:
            pTree.add_word(w)
        
        m, n = len(board), len(board[0])
        res, visited = set(), set()
        # define a recursive function that takes in coodinates and char at k
        def dfs(r, c, node, word):
            # return if out of bounds
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if board[r][c] not in node.children:
                return
            if (r, c) in visited:
                return 
            
            # add current coordinate to visited
            visited.add((r, c))
            # move onto the next node
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)
            # recurse on all 4 directions
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            # backtrack to try other route
            visited.remove((r, c))
        
        # iterate i from 0 to m
        for i in range(m):
            # iterate j from 0 to n
            for j in range(n):
                dfs(i, j, pTree.root, "")
        return list(res)