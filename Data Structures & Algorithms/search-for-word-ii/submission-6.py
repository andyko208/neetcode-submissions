# construct a trienode
class TrieNode:
    # define a constructor
    def __init__(self):
        self.children = {}
        self.isEnd = False

# class prefixTree
class PrefixTree:
    # define a constructor
    def __init__(self):
        self.root = TrieNode()
    # define a function to add words
    def addWord(self, word):
        cur = self.root
        # iterate through each char in words
        for c in word:
            # check if c is valid option
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        # reached the end of the word
        cur.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pTree = PrefixTree()
        # add all words to PrefixTree and construct a tree
        for word in words:
            pTree.addWord(word)
        
        # define a list to return
        res = []
        # keep a visited hashset
        visited = set()
        m, n = len(board), len(board[0])
        # define a recursive function is to find all words add to final list
        def dfs(i, j, node, word):
            # base case to append word to res
            # 1. if index goes out of bounds
            if i < 0 or i >= m or j < 0 or j >= n:
                return 
            # 2. if there is no child to walk through
            if board[i][j] not in node.children:
                return 
            # 3. if the node has been visited
            if (i, j) in visited:
                return

            # add (i, j) to visited
            visited.add((i, j))
            # update node pointer to next
            node = node.children[board[i][j]]
            # update the word
            word.append(board[i][j])
            # word is found
            if node.isEnd:
                res.append("".join(word))
                node.isEnd = False
            # try all 4 routes
            dfs(i+1, j, node, word)
            dfs(i-1, j, node, word)
            dfs(i, j+1, node, word)
            dfs(i, j-1, node, word)
            # backtracking
            visited.remove((i, j))
            word.pop()
            

        # call the dfs function
        # iterate i from 0 to m
        for i in range(m):
            # iterate j from 0 to n
            for j in range(n):
                dfs(i, j, pTree.root, [])
                visited = set()
        return res
